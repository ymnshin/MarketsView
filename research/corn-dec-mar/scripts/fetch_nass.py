"""Fetch USDA NASS Quick Stats raw corn data; preserves unmodified JSON with provenance.

Requires an API key supplied through NASS_API_KEY, not committed to Git.
The NASS load_time field is *not* automatically the market-available timestamp.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re

import requests

API_URL = "https://quickstats.nass.usda.gov/api/api_GET/"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--state", default="IA", help="Two-letter US state abbreviation")
    p.add_argument("--start-year", type=int, default=2015)
    p.add_argument("--end-year", type=int, default=2026)
    p.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "data/raw/nass")
    args = p.parse_args()
    api_key = os.getenv("NASS_API_KEY")
    if not api_key:
        p.error("Missing NASS_API_KEY environment variable. Obtain a free key from https://quickstats.nass.usda.gov/api")
    state = args.state.upper()
    if not re.fullmatch(r"[A-Z]{2}", state) or args.start_year > args.end_year:
        p.error("Invalid state or year range")
    timestamp = datetime.now(timezone.utc)
    args.out.mkdir(parents=True, exist_ok=True)
    for year in range(args.start_year, args.end_year + 1):
        query = {
            "key": api_key,
            "commodity_desc": "CORN",
            "sector_desc": "CROPS",
            "agg_level_desc": "STATE",
            "state_alpha": state,
            "year": str(year),
            "format": "JSON",
        }
        response = requests.get(API_URL, params=query, timeout=60)
        response.raise_for_status()
        payload = response.json()
        rows = payload.get("data")
        if not isinstance(rows, list):
            raise RuntimeError(f"Unexpected NASS response in {year}: {str(payload)[:250]}")
        if len(rows) >= 50000:
            raise RuntimeError(f"NASS row cap reached in {year}; filter by frequency/statistic")
        output = args.out / f"corn_{state}_{year}_{timestamp.strftime('%Y%m%dT%H%M%SZ')}.json"
        with output.open("w", encoding="utf-8") as f:
            json.dump({
                "provenance": {
                    "source_url": API_URL,
                    "retrieved_at_utc": timestamp.isoformat(),
                    "query_without_api_key": {k: v for k, v in query.items() if k != "key"},
                    "data_record_count": len(rows),
                    "market_available_at_utc": None,
                    "warning": "NASS load_time is not guaranteed to equal official public release time",
                },
                "raw_data": payload,
            }, f, ensure_ascii=False, indent=2)
        print(f"{output}: {len(rows)} records")


if __name__ == "__main__":
    main()
