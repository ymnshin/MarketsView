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
