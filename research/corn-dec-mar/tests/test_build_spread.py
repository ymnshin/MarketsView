"""No market data in tests: all settlements below are explicitly synthetic."""
from pathlib import Path
import sys
import unittest

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_spread import build_spread  # noqa: E402


class SpreadTests(unittest.TestCase):
    @staticmethod
    def master():
        return pd.DataFrame([
            {"contract_id": "ZC-2026-12", "delivery_year": 2026, "delivery_month": 12,
             "first_notice_date": "2026-11-30", "last_trade_date": "2026-12-14",
             "contract_size_bushels": 5000, "tick_size_cents_per_bushel": 0.25},
            {"contract_id": "ZC-2027-03", "delivery_year": 2027, "delivery_month": 3,
             "first_notice_date": "2027-02-26", "last_trade_date": "2027-03-12",
             "contract_size_bushels": 5000, "tick_size_cents_per_bushel": 0.25},
        ])

    @staticmethod
    def prices():
        return pd.DataFrame([
            {"trade_date": "2026-10-20", "contract_id": "ZC-2026-12", "settle_cents_per_bushel": 480},
            {"trade_date": "2026-10-20", "contract_id": "ZC-2027-03", "settle_cents_per_bushel": 490},
            {"trade_date": "2026-10-21", "contract_id": "ZC-2026-12", "settle_cents_per_bushel": 483},
            {"trade_date": "2026-10-21", "contract_id": "ZC-2027-03", "settle_cents_per_bushel": 490},
        ])

    def test_spread_and_pnl_sign(self):
        out = build_spread(self.prices(), self.master())
        self.assertEqual(list(out.spread_cents_per_bushel), [-10, -7])
        self.assertTrue(pd.isna(out.daily_mark_to_market_usd_one_pair.iloc[0]))
        self.assertEqual(out.daily_mark_to_market_usd_one_pair.iloc[1], 150.0)

    def test_duplicate_rejected(self):
        inp = pd.concat([self.prices(), self.prices().iloc[[0]]], ignore_index=True)
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            build_spread(inp, self.master())

    def test_missing_leg_is_not_filled(self):
        inp = self.prices().drop(index=1)
        out = build_spread(inp, self.master())
        self.assertEqual(len(out), 1)
        self.assertEqual(out.trade_date.iloc[0], "2026-10-21")

    def test_delivery_risk_cutoff(self):
        after = pd.DataFrame([
            {"trade_date": "2026-11-25", "contract_id": "ZC-2026-12", "settle_cents_per_bushel": 480},
            {"trade_date": "2026-11-25", "contract_id": "ZC-2027-03", "settle_cents_per_bushel": 490},
        ])
        inp = pd.concat([self.prices(), after], ignore_index=True)
        out = build_spread(inp, self.master(), exit_buffer_days=10)
        self.assertEqual(len(out), 2)


if __name__ == "__main__":
    unittest.main()
