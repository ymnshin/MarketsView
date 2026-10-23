"""Build annual CBOT corn Dec-minus-next-Mar spreads from contract-specific settlements.

Inputs are real data supplied by the user. This script does not download market prices
or claim historical backtest performance. All amounts are expressed in cents/bushel.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

REQUIRED_PRICES = {"trade_date", "contract_id", "settle_cents_per_bushel"}
REQUIRED_MASTER = {
    "contract_id", "delivery_year", "delivery_month", "first_notice_date",
    "last_trade_date", "contract_size_bushels", "tick_size_cents_per_bushel",
}


def build_spread(prices: pd.DataFrame, master: pd.DataFrame, *, exit_buffer_days: int = 10) -> pd.DataFrame:
    """Return joined daily Dec-Mar spreads and one-pair daily mark-to-market PnL.

    exit_buffer_days is CALENDAR days before first-notice date, not business days.
    Both legs must be present on the same date, and the annual contract pairs
    must be in the instrument master. No price is forward-filled.
    """
    if exit_buffer_days < 1:
        raise ValueError("exit_buffer_days must be >= 1 (calendar days)")
    if not REQUIRED_PRICES <= set(prices.columns):
        raise ValueError(f"Missing price columns: {sorted(REQUIRED_PRICES-set(prices.columns))}")
    if not REQUIRED_MASTER <= set(master.columns):
        raise ValueError(f"Missing master columns: {sorted(REQUIRED_MASTER-set(master.columns))}")

    p = prices.copy()
    m = master.copy()
    p["trade_date"] = pd.to_datetime(p["trade_date"], errors="raise").dt.normalize()
    m["first_notice_date"] = pd.to_datetime(m["first_notice_date"], errors="raise").dt.normalize()
    m["last_trade_date"] = pd.to_datetime(m["last_trade_date"], errors="raise").dt.normalize()
    p["settle_cents_per_bushel"] = pd.to_numeric(p["settle_cents_per_bushel"], errors="raise")
    m["contract_size_bushels"] = pd.to_numeric(m["contract_size_bushels"], errors="raise")
    m["delivery_year"] = pd.to_numeric(m["delivery_year"], errors="raise").astype(int)
    m["delivery_month"] = pd.to_numeric(m["delivery_month"], errors="raise").astype(int)

    if p.empty:
        raise ValueError("No price observations; supply contract-specific settlement CSV")
    if p[["trade_date", "contract_id", "settle_cents_per_bushel"]].isna().any().any():
        raise ValueError("Null price fields are not allowed")
    if (p["settle_cents_per_bushel"] <= 0).any():
        raise ValueError("Nonpositive corn settlements need investigation")
    if p.duplicated(["trade_date", "contract_id"]).any():
        raise ValueError("Duplicate trade_date × contract_id in prices")
    if m.duplicated(["contract_id"]).any():
        raise ValueError("Duplicate contract_id in master")
    if not set(p["contract_id"]).issubset(set(m["contract_id"])):
        raise ValueError("Some price contract_ids are missing from master")
    if (m["contract_size_bushels"] != 5000).any():
        raise ValueError("The model currently supports only full-size 5000-bushel ZC")

    d = p.merge(
        m[["contract_id", "delivery_year", "delivery_month", "first_notice_date", "last_trade_date"]],
        on="contract_id", how="inner", validate="many_to_one",
    )
    # Exclude data too close to the physical-delivery window.
    d = d.loc[(d["first_notice_date"] - d["trade_date"]).dt.days > exit_buffer_days].copy()
    d = d.loc[d["trade_date"] <= d["last_trade_date"]]

    dec = d.loc[d["delivery_month"] == 12, ["trade_date", "delivery_year", "settle_cents_per_bushel", "first_notice_date"]].copy()
    mar = d.loc[d["delivery_month"] == 3, ["trade_date", "delivery_year", "settle_cents_per_bushel"]].copy()
    dec = dec.rename(columns={"delivery_year": "crop_year", "settle_cents_per_bushel": "dec_settle", "first_notice_date": "dec_first_notice"})
    mar = mar.rename(columns={"delivery_year": "march_year", "settle_cents_per_bushel": "mar_settle"})
    mar["crop_year"] = mar["march_year"] - 1
    if dec.duplicated(["trade_date", "crop_year"]).any() or mar.duplicated(["trade_date", "crop_year"]).any():
        raise ValueError("Multiple legs per trade_date/crop_year; check master")
    merged = dec.merge(mar.drop(columns="march_year"), on=["trade_date", "crop_year"], how="inner", validate="one_to_one")
    if merged.empty:
        raise ValueError("No matched December/next-March daily observations")
    merged = merged.sort_values(["crop_year", "trade_date"]).reset_index(drop=True)
    merged["spread_cents_per_bushel"] = merged["dec_settle"] - merged["mar_settle"]
    merged["days_to_dec_first_notice"] = (merged["dec_first_notice"] - merged["trade_date"]).dt.days
    merged["daily_mark_to_market_usd_one_pair"] = merged.groupby("crop_year")["spread_cents_per_bushel"].diff() * 50.0
    merged["dec_first_notice"] = merged["dec_first_notice"].dt.strftime("%Y-%m-%d")
    merged["trade_date"] = merged["trade_date"].dt.strftime("%Y-%m-%d")
    return merged


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prices", required=True, type=Path, help="User-provided futures_daily.csv")
    parser.add_argument("--master", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--exit-buffer-days", type=int, default=10, help="Calendar days ahead of FND")
    args = parser.parse_args()
    result = build_spread(pd.read_csv(args.prices), pd.read_csv(args.master), exit_buffer_days=args.exit_buffer_days)
    args.out.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.out / "spreads.csv", index=False)

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5))
    for year, group in result.groupby("crop_year", sort=True):
        ax.plot(group["days_to_dec_first_notice"], group["spread_cents_per_bushel"], label=str(year))
    ax.axhline(0, linewidth=0.8)
    ax.invert_xaxis()
    ax.set_xlabel("Calendar days until Dec first notice")
    ax.set_ylabel("Dec minus next Mar (cents / bushel)")
    ax.set_title("Corn Dec-next-Mar spread (contract-specific settlements)")
    ax.legend(title="Dec delivery year")
    fig.tight_layout()
    fig.savefig(args.out / "seasonal_spreads.png", dpi=160)
    plt.close(fig)
    print(f"Saved {len(result)} matched rows in {args.out}. This is descriptive, not a backtest.")


if __name__ == "__main__":
    main()
