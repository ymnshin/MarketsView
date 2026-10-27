# Brent–WTIの価格差は裁定できるか？（2026-10-23）

## 最初の疑問
> WTIは米国の代表的な原油、Brentは国際価格の基準。原油価格の差は裁定できそう？ 米国がロシアから燃料を買うほど困っているなら、Brentの高値が続く中でWTIは上がる方向になる？

## 結論
- **現物裁定は存在するが、無条件の利益ではない**。地域・品質・時点が異なり、パイプラインやタンカーの輸送費、保険料、港湾費、精製適性、受渡期間が必要。
- **先物でWTIロング＋Brentショート**は「Brent−WTIスプレッドが縮小する」という**相対価値トレード**であって、リスクのない裁定ではない。
- **ロシアからの輸入は原油ではなく軽油**。米国内の製品需給問題を、そのままWTI原油の不足と読み替えるのは誤り。
- **縮小の経路は2つ**：WTIの相対的上昇、Brentの相対的下落。中東の供給混乱が解消すればBrentの下落で縮小する可能性もある。
- 船舶運賃が高止まりして輸出裁定が難しければ、スプレッドは大きく開いたまま続く可能性がある。

## 観測事実と価格（同時刻でない数値には注意）
- Reuters（2026-10-23の市況記事中の取引中参考値）：Brent **$114.99/bbl**、WTI **$101.27/bbl**、単純差 **約$13.72/bbl**。厳密な取引可能スプレッドではない。
- 2026-10-22の**同じ2026年12月限**の報道終値では、Brent **$113.17**、WTI **$99.47**、差 **$13.70/bbl**。
- 先物は必ず**限月・観測時刻**を揃える。異なる限月を比較するとバックワーデーション／コンタンゴの差が混ざる（EIA）。
- リアルタイムの執行価格はビッド／アスク、手数料、証拠金、ロールコストを別途確認。

## 金融的なスプレッド取引の損益
`S_t = Brent_t - WTI_t`

WTIを1バレル買い、Brentを1バレル売る組合せの損益は、

`PnL = (WTI_1 - WTI_0) - (Brent_1 - Brent_0) = S_0 - S_1`

仮に `S_0=14` から `S_1=9` に縮めば **+$5/bbl**、`S_1=20` に拡大すれば **-$6/bbl**。ICEにもBrent–WTIのスプレッド取引商品がある（複数ポジションの組合せである点に注意）。

## 現物裁定の概念
WTI系原油を米国内で調達し、沿岸へ運び、海外製油所に販売するときの採算は次の比較で決まる。

`海外での品質調整後販売価格 − 米国沿岸でのWTI系調達価格 − 運賃・保険料・港湾費・時間費用 > 0`

重要：NYMEX WTIの受渡地点は内陸の**Cushing（オクラホマ州）**。米国沿岸で輸出される**WTI Midland**などとは同じ値段ではない。先物の Brent−WTI 差がそのまま物理的裁定利益にはならない。

2026年10月8日のS&P Global分析では、タンカー運賃高騰を受けて米国湾岸→アジア向けのスポット裁定が成立しにくい一方、欧州向けでは依然として裁定機会があるとしていた。**どの航路も同じではない**。

## 3つのシナリオ
| シナリオ | 価格の想定 | Brent−WTIへの含意 |
|---|---|---|
| 米国産原油への海外需要拡大・輸送制約緩和 | WTIが相対的に上昇 | 縮小 |
| 中東の供給不安・海上輸送障害が継続 | Brentに高いリスクプレミアム、運賃高騰 | 拡大・高止まりの可能性 |
| 中東の輸送が正常化 | Brentが相対的に下落 | 縮小 |

## 検証する仮説と反証条件
**H1：米国産原油の輸出裁定が機能してWTIが相対的に上昇する。**
- 追跡：Brent−WTI同限月差、WTI Cushing対WTI Houston/Midland価格差、米国原油輸出量、欧州向け運賃
- 反証：輸出採算が改善せず輸出量も増えない／スプレッドが拡大し続ける

**H2：価格差の主因は国際側の供給不安・物流プレミアム。**
- 追跡：ホルムズ・紅海の通航量、タンカー運賃、Brent−WTI差、原油輸出停止量
- 反証：物流が正常化しても差が縮まず、米国内在庫・品質要因で説明される

**H3：ロシア産軽油の輸入がWTI上昇につながる。**
- **直接の因果には根拠が弱い**。むしろ軽油供給増は軽油価格・精製マージンを下押しし得る。
- 観測：米国ULSD価格、ULSD−WTIクラックスプレッド、軽油在庫、製油所稼働率、WTI価格
- 反証：軽油価格だけが下がり原油価格が追随しない、またはWTIが下がる

## 参考資料
1. Reuters（2026-10-23）：https://www.reuters.com/business/energy/oil-little-changed-supply-concern-lingers-amid-houthi-attacks-saudi-arabia-2026-10-23/
2. Reuters（ロシア産軽油タンカー）：https://www.reuters.com/business/energy/tanker-carrying-40000-t-russian-diesel-heads-new-york-after-putin-trump-deal-2026-10-23/
3. 米国EIA（先物限月を揃えて比較する必要性）：https://www.eia.gov/TodayinEnergy/detail.php?id=24692
4. ICE（Brent/WTIスプレッド取引）：https://www.ice.com/products/1242/specs
5. CME（CushingとWTI）：https://www.cmegroup.com/education/articles-and-reports/why-cushing-matters-a-look-at-the-wti-benchmark
6. S&P Global（2026-10-08、輸送費上昇と輸出裁定）：https://www.spglobal.com/energy/en/news-research/latest-news/shipping/100826-appetite-for-us-crude-oil-exports-climb-despite-high-freight
7. EIA（軽油需給）：https://www.eia.gov/energyexplained/diesel-fuel/where-our-diesel-comes-from.php

> 個人学習用。市況データは記事掲載時点の参考値で、発注可能な気配・先物の清算値とは異なる。


## 2026-10-24 07:47 JST 追加照合
Reutersの**2026/10/23最終市況記事**ではBrent $116.72、WTI $103.27と報じられ、WSJの当日記事で**両方が2026年12月限**と確認された。算術差は**$13.45/bbl**だが、ICEとNYMEXの**同時刻の気配値ではなく、別々の清算値**。この差を厳密な裁定利益・執行価格と扱わず、元の縮小仮説は**未判定**のまま。今後は同一UTC時刻のbid/askと湾岸輸送コストで比較。
- [Reuters 10/23 最終報道](https://www.reuters.com/business/energy/oil-little-changed-supply-concern-lingers-amid-houthi-attacks-saudi-arabia-2026-10-23/)
- [WSJ 10/23 両者の12月限確認](https://www.wsj.com/world/middle-east/oil-prices-rise-as-middle-east-risks-persist-c1262364)
- [詳細記録](../daily/2026-10-24-review-0747-jst.md)

## 2026-10-26 07:44 JST：取引時間の一次資料照合（裁定未判定）
[ICE Brent先物の公式仕様](https://www.ice.com/products/219/Brent-Crude-Futures)と[Brent/WTI上場スプレッド仕様](https://www.ice.com/products/1242/specs)によれば、日曜の取引開始は**23:00ロンドン時間**、プレオープンは22:00。英国冬時間移行後の**2026/10/26 08:00 JST**がICEの取引開始。対して[CME WTI公式](https://www.cmegroup.com/education/courses/event-contracts-underlying-markets/wti-overview)では日曜**17:00米中部時間**から（10/26 07:00 JST）。**07:44 JSTはICE Brentの取引開始前**のため、同2026年12月限・同一UTC時刻・両脚bid/askに基づく新たな執行可能スプレッドは取得できない。10/23報道清算値差$13.45を新価格に流用しない。今後は08:00 JST以降の取引所提示の執行可能な両脚気配、板・コスト・海運物流を照合する。**仮説判定：未判定／変化なし**。詳細は[当回レビュー](../daily/2026-10-26-review-0744-jst.md)。


## 2026-10-27 07:44 JST：10/26米国終値の確定と限月差の注意
- [Reuters 10/26引け](https://www.reuters.com/business/energy/oil-prices-down-almost-1-early-trading-2026-10-25/)はBrent **$115.81（-0.8%）**、WTI **$101.76（-1.46%）**。[WSJ 10/26 15:55 ET](https://www.wsj.com/finance/commodities-futures/oil-declines-on-likely-technical-correction-ad4be59e)がICE Brent **2026年12月限 $115.81**と**2027年1月限 $110.74**を区別。WTI側も当日の2026年12月限（CLZ26）終値に相当する（[限月別照合](https://www.barchart.com/futures/quotes/CLZ26)）。よって同じ12月限どうしの**報道終値の算術差 $14.05/bbl**を参考記録する。
- 10/23の同月報道終値差$13.45との差**+$0.60**は、異なる取引所の**清算時刻・算出規則をそろえた同時刻の実売買気配ではない**ため、執行可能スプレッドの拡大や裁定成績を示さない。**輸出裁定縮小仮説は未判定**。
- **反証条件/次点検**：同一UTC秒のICE/NYMEX 2026年12月限 bid/ask（両脚のサイズ・約定可能性）、WTI Midland/MEH価格、米国欧州向け実運賃・保険・米国原油輸出量で、実物裁定採算と価格差を比較する。2027年1月限Brent $110.74を12月限WTIと差し引かない。
- [本日の定点レビュー](../daily/2026-10-27-review-0744-jst.md)参照。


## 2026-10-27 23:50 JST：場中価格の更新と同期気配未取得
[Reuters 10/27記事の直近価格観測13:11 GMT（22:11 JST）](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)ではBrent $114.81、WTI $100.98。前回19:52レビューに記した**09:18 GMT**の$116.26/$102.16と観測時刻が違い、**同一UTC時点・同一2026/12限の執行可能bid/askを両市場で確認できていない**。報道値の算術差を縮小裁定の実行損益には使用しない。**判定：未判定**。反証・次回：同時刻ICE/NYMEX両脚価格、WTI Midland/MEHの現物条件、保険・輸送/港湾費、米輸出数量が揃っても持続的な純裁定余地や輸出増が確認されないこと。[23:50レビュー](../daily/2026-10-27-review-2350-jst.md)。
