# データソース台帳（2026-10-23）

**対象：** CBOT/CME ZC・12月限と翌3月限。同じ日に観測した個別限月の清算値で価格差を作る。

| データ | 公式入口 | 公表・取得上の注意 |
|---|---|---|
| 個別限月の清算値 / 出来高 / 建玉 | [CME Settlements](https://www.cmegroup.com/markets/agriculture/grains/corn/settlements.html) | 日次閲覧可能な範囲・長期履歴の購入と転載条件は別。連続価格だけでは不可 |
| 契約・受渡日 | [CME Specs](https://www.cmegroup.com/markets/agriculture/grains/corn/specs.html) / [Calendar](https://www.cmegroup.com/markets/agriculture/grains/corn/calendar.html) | 2026/12第一通知日11/30、最終取引日12/14。2027/03第一通知日2/26、最終取引日3/12 |
| 公表時点の穀物需給・在庫予測 | [USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report) | 2010年以降の過去公表時点のデータを含む。レポートの参照期間とリリース時刻は別 |
| 作付・単収・進捗・Grain Stocks | [NASS Quick Stats](https://quickstats.nass.usda.gov/api) | 無料APIキー。1要求で最大50,000件。load_timeだけで市場の公表日時を断定しない |
| 地域別現物価格・基差 | [USDA AMS](https://mymarketnews.ams.usda.gov/mymarketnews-api) | 現物の品質・場所と比較先物限月が重要 |
| 輸出販売・船積み | [USDA FAS](https://www.fas.usda.gov/data) | 参照週と報告日を区別 |
| エタノール・米国原油など | [EIA Open Data](https://www.eia.gov/opendata/) | 無料API、系列ごとの公表頻度・改訂に注意 |
| 投機筋などのポジション | [CFTC COT](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm) | 火曜ポジション、通常金曜公表。特定限月間の直接ポジションではない |
| 短期金利 | [FRED API](https://fred.stlouisfed.org/docs/api/fred/series_observations.html) | 改訂がある統計はヴィンテージに注意 |

## 必須スキーマ
- instrument_master: contract_id / delivery_year / delivery_month / first_notice_date / last_trade_date / contract_size / tick_size
- futures_daily: trade_date / contract_id / settle_cents_per_bushel / volume / open_interest / source / retrieved_at_utc
- fundamental_releases: series_id / reference_period / release_timestamp_utc / available_timestamp_utc / value / vintage
- features_daily: decision_timestamp / spread / carry_utilization / stocks_to_use_latest_known / basis / rate
- paper_trades: signal_time / entry_time / entry_spread / exit_spread / size / MAE / MFE / pnl / postmortem

## 実データを入れる前のチェック
1. 米セント/ブッシェル単位を固定（例：465.25）。
2. trade_date×contract_idを一意にする。
3. 12月限と翌3月限の**同日の観測**だけ結合。欠損を勝手に補間しない。
4. first noticeより早く取引を閉じる。
5. 公表情報は available_timestamp_utc 以前の意思決定に混ぜない。
6. 情報発表後にしか約定できない価格で実行したことにしない。
7. データ利用権限を確認。APIキーと有料価格の生データは公開しない。

## 不足しているもの
現時点では**過去の個別限月清算値の実測CSVが未取得**であり、リターン、平均回帰、予測成績は**未検証**。
大学のデータ端末やブローカーの履歴を優先して確認し、十分な年数が確保できなければ有料のCME DataMineなどを検討する。
