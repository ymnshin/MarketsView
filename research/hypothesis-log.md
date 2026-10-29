# 仮説ログ

市場観察では「当たったかどうか」だけでなく、どの条件で説明が崩れたかを残す。

| 日付 | 仮説 | 観測する指標 | 反証条件 | 判定 |
|---|---|---|---|---|
| 2026-10-23 | 中東の供給不安が原油高を支えている | Brent、実生産量、輸出量、船舶保険 | 供給が正常化しBrent・輸送プレミアムが継続的に低下 | 未判定 |
| 2026-10-23 | 迂回増加は海運会社の収益に追い風 | トンマイル、TCE、燃料費・保険料、契約別収益 | 運賃増がコスト増を補えずTCE・営業利益が改善しない | 未判定 |
| 2026-10-23 | AI信用不安は半導体株を下押しする | SOX、企業社債スプレッド、日経平均とTOPIX | 信用スプレッド縮小と半導体株の持続的反発 | 未判定 |
| 2026-10-23 | Brent–WTIスプレッドは米国産原油の輸出裁定によって縮小する | 同限月Brent–WTI、WTI Midland/MEH、欧州向け運賃、米国原油輸出量 | 運賃高止まり・輸出量停滞の中でスプレッドが拡大継続 | 未判定 |
| 2026-10-23 | トウモロコシ12月−翌3月限の保管キャリー超過が20営業日後の価格差上昇を予測する | 個別限月清算値、WASDEヴィンテージ、在庫、基差、保管・金利費用 | 年度外検証で不安定／取引費用控除後に再現性がない | データ未取得・未判定 |

| 2026-10-24 | 中東情勢のイベントで原油の実現変動が購入時のストラドル費用を上回る | 同限月WTIオプションのプレミアム・IV・期末先物価格・売買費用 | 結果の値動きが購入時の損益分岐幅を超えず、買いプレミアムを回収できない | オプション価格未取得・未判定 |
| 2026-10-24 | 短期の原油供給ショックでWTI近月−6か月期先スプレッドが拡大する | 個別限月清算値、原油在庫、供給停止量、ニュース公表時刻 | 期先が相対的に大きく上昇／スプレッドが縮小する | 未判定 |
| 2026-10-24 | 中東供給混乱はスポットタンカーに増益、長期契約・自動車船には効果が弱い | 船種別TCE・スポット稼働日数・3社事業別経常利益・ONE利益・燃油BAF回収期間 | 運賃上昇でも稼働縮小・自社負担増でTCE/実現利益が低下、または長期契約で市況が転嫁されない | 初期資料は支持、10月追加ショックは未判定 |
| 2026-10-24 | 中東混乱下のタンカー運賃高騰はスポット契約比率が高い船主の利益を増やす | ECO/FRO/DHTの未成約スポット稼働日数・TCE・保険費用・四半期実績 | 成約稼働日数の減少や費用増で実現TCEが伸びない、または高値が既に固定済み | DHT 10/12成約情報は支持、Q4利益は未確定 |

[関連ノート](../topics/2026-10-23-brent-wti-spread-arbitrage.md)

## 検証ルール
- 価格データは市場・タイムゾーン・終値の定義をそろえる。
- 仮説を書いた**後**に結果を記録し、後知恵の書き換えを避ける。
- 株価の相関だけで因果関係を断定しない。
- 反証の有無とは別に、新しいショックや競合仮説を記録する。

[トウモロコシ研究計画](corn-dec-mar/README.md)

[中東情勢と方向を当てない取引](../topics/2026-10-24-middle-east-outcomes-volatility-strategies.md)

[バックワーデーションと原油カレンダースプレッド](../topics/2026-10-24-crude-oil-calendar-spread-backwardation.md)

[中東危機で利益を得る海運事業者の条件：世界 vs 日本](../topics/2026-10-24-global-vs-japan-shipping-middle-east.md)

[原油タンカーのスポット受益企業研究](../topics/2026-10-24-spot-tanker-beneficiaries.md)

## 2026-10-24 03:43 JST 定点照合（元の仮説は上記に保持）
[日時・報道・条件・反証を分離した検証ノート](../daily/2026-10-24-review-0343-jst.md)を追加した。

- **中東供給リスク**：Reuters 10/23 18:06 UTCでBrent $116.35、WTI $102.97。値上がりという中間観測は整合的だが、供給量減少・持続期間は**未判定**。同限月スプレッド計算には使わない。
- **Brent–WTI輸出裁定**：同限月・同時刻の公式気配値未確認につき**未判定**。
- **タンカー・国内海運**：以前の船主決算と成約は部分的支持、10/23以降の追加実績と日本企業の増分利益は**未判定**。
- **ロシア産軽油**：10/22に積み出した4万トンの11/7到着予定と後続便方針が報じられた。到着・米軽油価格下落・WTI波及は**未判定**。
- **AI信用とSOX**：10/22 Meta CDS 114.79bp、10/23 SpaceX/Oracle/Meta社債スプレッド拡大。信用ストレスの**中間指標は支持**、株価下落への因果は**未判定**。
- **コーン12月−翌3月**：個別限月の複数年清算値CSVがなく、**データ未取得・未判定**。CME公式カレンダーで受渡関連日を照合済み。


## 2026-10-24 07:47 JST 定点照合（03:43の記録・元仮説は保持）
[新しい終値・週報・船舶位置・信用市場を照合したレポート](../daily/2026-10-24-review-0747-jst.md)を追記。

- **中東原油**：10/23のReuters報道清算値はBrent **$116.72**、WTI **$103.27**（ともに2026年12月限）。原油上昇は供給不安と整合的。ただし中東の純減産規模と価格上昇の持続性は**未判定**。
- **Brent–WTI**：同じ12月限での報道清算値の算術差 **$13.45/bbl**。両市場の清算時点は未照合で、**同限月・同時刻の取引可能スプレッドではない**。縮小裁定は**未判定**。
- **海運・利益**：10/23のBaltic週報では**VLCCの一部代表航路は下落、製品船の一部航路は上昇**。船種・航路別に影響が異なる仮説は**支持**、スポット船主と日本3社の新たな確定利益は**未判定**。有料指数の数列は転載しない。
- **ロシア軽油**：10/23初報のNY目的地は、後続のAISで**FOR ORDERS**に変更。積出しは支持、米国荷揚げ・米ULSD価格への影響は**未判定**。
- **AI信用**：10/23にもAI関連企業の社債スプレッド拡大。**信用ストレスの持続を部分的支持**、SOXへの因果は**未判定**。
- **コーン12月−翌3月保管キャリー**：個別限月の単日気配表示はあっても複数年度の清算値履歴・保管費等がなく**データ未取得・未判定**。

## 2026-10-24 11:44 JST 定点照合（過去の仮説・判定行は保持）
[事実・出典・監視条件を分離した11:44レビュー](../daily/2026-10-24-review-1144-jst.md)を追記した。

- **中東航行リスク**：Reuters 10/23 14:58 UTCの10月船舶攻撃**28件（確認・報告ベース）**、VLCCの損傷30隻超（10月11隻）を確認。**安全リスク存在を支持**、恒久船腹減・原油純供給減・長期高運賃の持続性は**未判定**。反証：船腹回復・保険料と実現TCEの低下、荷動き減による収益悪化。
- **ロシア産軽油**：Agioi FanendesのAISは`FOR ORDERS`とする先行検証を保持。追加で**PVT Azura**のNorfolk向けAIS/11月2日ETAの報道、露副首相の**3隻航行**発言、米財務省OFACの10/9付General License 135を照合。**輸入実績と価格効果は未判定**。反証/確認：実際の荷揚げと通関データ、ULSD価格・クラックを比較。
- **Brent–WTI**：2026/10/23同12月限の報道清算値の算術差**$13.45**は前回と同じ。**同一UTC時刻のbid/ask未取得・裁定未判定**。
- **海運利益**：船種・航路・契約で異なるとの仮説は**部分的支持**、日本3社とスポットタンカー船主の追加Q4利益は**未判定**。損傷船数を直ちに収益増とみなさない。
- **AI信用とSOX**：同一期限で比較できる新規信用価格を未取得。**ストレス部分支持、株価との因果は未判定**。
- **トウモロコシ12月−翌3月の保管キャリー**：研究用の複数年度価格系列を取得できず**データ未取得・未判定**。結果は作成しない。


## 2026-10-24 15:44 JST 定点照合（原仮説は保持）
[今回の検証記録](../daily/2026-10-24-review-1544-jst.md)：**直前11:44時点からの相場・輸送・確定損益の新規検証結果はなし**。公表済み一次資料から未収録だった基準点を追加。

- **米ロシア産軽油**：EIAが10/20公表した10/19週の全米軽油小売価格（税含む）は **$6.276/gal**、10/12週 **$6.179**。実際の輸入前の観測基準であり、ロシア産軽油の米国荷揚げ・ULSD先物への因果効果は**未判定**。
- **AI信用**：Metaの10/21 Q3公式開示で2026年設備投資計画 **$135–145bn**、Q3 FCF **−$2.12bn**、Class C議決権なし株導入計画を確認。既存株主への株式配分自体は**資本調達・債務削減ではない**。信用スプレッドやSOXへの因果・反証は**未判定**。
- **Brent–WTI、タンカー、海運利益**：同一UTC時刻の同限月bid/ask、新しい実現TCEや企業決算は未確認。既存の「部分支持／裁定・利益未判定」を維持。
- **トウモロコシ12月−翌3月保管キャリー**：実価格履歴はなく**データ未取得・未判定**。合成テスト例を実証結果と混同しない。


[AI信用市場：Metaの資本政策・FCFと株式分割を区別](../topics/2026-10-24-ai-credit-and-meta-funding.md)


## 2026-10-24 19:50 JST 定点照合（元の仮説は保持）
[19:50レビュー](../daily/2026-10-24-review-1950-jst.md)を追加。**新しい10月24日の取引所清算値ではなく、10月23日付の未記録資料を照合した。**

- **AI信用**：Reuters 10/23米国午後（LSEG）ではMeta **5年CDS 約123bp・当日比0.3%縮小**。一方WSJ/MarketAxess 10/23では**Meta 2031年債スプレッド75bp、前日比+5bp**、Oracle同債263bp（+4bp）、SpaceX 2031年債228bp（前日205bp）。**信用ストレスの存在は部分支持、全指標一律拡大は否定、SOX下落への因果は未判定**。10/22 **Markit**のMeta 114.79bpと10/23 **LSEG**の123bpを差し引いて前日変化としない。**反証**：同一銘柄・商品・ベンダーの系列で信用悪化が持続せず、SOXとの市場調整後の予測関係も再現しない。出典は詳細ノートに記載。
- **コーン12月−翌3月**：MarketWatch掲載**10/23の同日限月別清算値**はZCZ26 **456.00¢/bu**、ZCH27 **470.25¢/bu**、したがって定義した**C=−14.25¢/bu**。単日カーブがコンタンゴである観察のみ。保管キャリーの理論値・20営業日後の変化・取引費用控除後の成果は **データ未取得・未判定**。**反証**：年度外で予測力・費用控除後優位性が消える／符号が反転。
- **Brent–WTI／中東・タンカー／国内海運／ロシア産軽油**：前回から同限月・同UTC時刻の両脚気配、追加の確定TCE・部門損益、米国のロシア軽油荷揚げを確認できず、**既存判定を変更しない**。船舶のAIS予定地と荷揚げ実績を区別。

## 2026-10-24 週末検証計画（新仮説・原記録維持）
[週末レビュー](../daily/2026-10-24-weekend-research-plan.md)に、**10/23日経平均の下落後の戻りはショートカバー／パッシブ買い中心だったか**という仮説を追加。**未判定**。検証：同一時間帯の日経225先物12月限の価格・出来高、建玉の変化、TOPIX・銘柄騰落と指数寄与度。反証候補：幅広い銘柄で持続的買いが入り、建玉が増加するなど買い戻し単独では説明しにくい場合。**建玉増減だけでショートカバーを確証できない**。AI信用→日本半導体、船種別TCE→海運利益も継続監視。週末の新しい市場データは確認しておらず、既存の仮説判定は維持。トウモロコシは**データ未取得・未判定**。

## 2026-10-24 23:47 JST 週末再照合（過去の判定は維持）
[23:47レビュー](../daily/2026-10-24-review-2347-jst.md)：**新規の市場清算値ではなく、10/24の安全保障・環境リスクに関する報道を追加確認**。

- **サウジ・ヤンブー周辺**：Reuters **10/24 08:34 UTC**、サウジ主導連合発表としてターイフ／ヤンブー方面への**弾道ミサイル2発の迎撃**を報道。**航行・エネルギー設備リスクの継続を支持**。ただし**施設損傷・実輸出減は未確認**で、原油供給減仮説は**未判定**。反証：ヤンブー出荷量の正常化、保険・運賃プレミアムの解消。出典：[Reuters](https://www.reuters.com/world/middle-east/saudi-civil-defense-says-danger-passed-after-brief-alerts-mecca-jeddah-taif-2026-10-24/)。
- **UAE沿岸油流出**：Reuters **10/24 12:28 UTC**、前日の海岸閉鎖措置に続いて**ラアス・アル＝ハイマでも海岸全域の閉鎖を発表**。**船名・流出原因は当局未特定**。海上環境リスクの存在は支持するが、**原油輸出量・タンカー運賃・日本海運会社利益への定量効果は未判定**。反証：港湾・タンカー稼働に支障がなく、運航費用・輸出量に持続的影響がない。出典：[Reuters](https://www.reuters.com/world/middle-east/uaes-ras-al-khaimah-shuts-all-beaches-neighbours-grapple-with-oil-spill-2026-10-24/)。
- **Brent–WTI**：10/23同12月限の報道清算値差**$13.45/bbl**は引き続き**同時刻の取引可能差ではない**。裁定・スプレッド縮小は**未判定**。
- **ロシア産軽油・AI信用・船主利益**：24日夜時点で前回にない米国荷揚げの確証、同条件CDS/OAS、追加の実現TCEや日本3社の確定利益を取得できず、**既存判定を維持**。
- **トウモロコシ12月限−翌3月限**：単日の清算値比較から複数年度の保管キャリー検証は不可能。価格履歴・保管費等は依然**データ未取得・未判定**。取引費用控除後の年度外結果がなければ支持としない。

## 2026-10-25 03:50 JST 定点照合（原仮説・過去記録は維持）
[今回のレビュー](../daily/2026-10-25-review-0350-jst.md)で、10/24付Reutersの現在の掲載内容から**フーシ派がYanbu Aramco施設・Rabigh製油所・東西パイプライン・原油ポンプ場を標的としたと主張**した点と、イエメン政府側が**アデン沿岸警備施設に弾道ミサイル3発が命中**したと報告した点を新たに記録。**標的主張は命中・生産停止・輸出減の確認ではない。** 安全保障リスクは支持、追加の実供給減・Brent高値持続・海運利益増は**未判定**。反証・確認：各施設の操業・原油積出実績、航路別通航数・実現TCE、保険費用と船社損益。

ロシア軽油船については10/23付Rivieraが船主Eastmedに取材し、**荷揚げ港は未確定（for orders）**と確認したことを追加照合。米国輸入・ULSD価格効果は**未判定**。Brent–WTIは**同限月・同UTC時刻bid/ask未取得で裁定未判定**、AI信用→SOXの因果も**未判定**、トウモロコシは複数年度清算履歴の**データ未取得・未判定**を維持。今回の詳細出典と照合時刻はリンク先に記載。

## 2026-10-25 07:43 JST 定点照合（原仮説・過去判定は保持）
[07:43レビュー](../daily/2026-10-25-review-0743-jst.md)を追加。**直前03:50からの新しい取引所清算値・確定出荷減・海運実現利益の確認なし。** 以前公表されたReuters資料を今回新規照合した：10/24 16:03 UTCの米国家情報長官による10/23付警告メモと、10/23 16:54 UTCのイラン高官による湾岸海底通信ケーブル攻撃の**条件付き計画の主張**。米政府の警戒・通信インフラへの潜在リスクは追加材料だが、**新規攻撃の成功、石油施設の停止、通信障害、AI企業のCDS変化の確認ではない**。中東の安全保障リスクは支持、原油純供給減・Brent–WTI輸出裁定・ロシア軽油米国荷揚げ・船主のQ4実現増益・AI信用→SOX因果は**未判定を維持**。**Brent $116.72－WTI $103.27＝$13.45/bblは10/23同2026年12月限の異市場報道清算値の差であり同時刻気配ではない。** コーンは依然**データ未取得・未判定**。反証条件と次の観測はレビュー本文。出典：[Reuters 10/24米当局警告](https://www.reuters.com/world/middle-east/iran-has-ramped-up-efforts-target-us-personnel-intelligence-memo-warns-2026-10-24/)・[Reuters 10/23海底通信ケーブル](https://www.reuters.com/world/middle-east/iran-has-detailed-plans-hit-gulf-undersea-cables-if-war-resumes-officials-say-2026-10-23/)。

## 2026-10-25 11:52 JST 定点照合（元の仮説は保持）
[11:52レビュー](../daily/2026-10-25-review-1152-jst.md)を追記。**Reuters 2026-10-24 23:56 UTC（10/25 08:56 JST）**は、リヤドのキング・ハーリド国際空港の一部ターミナルについて10/25からの運航再開計画が示された後、フーシ派が**同空港を引き続き標的とするとの警告を更新**したと報道。**航空インフラの安全保障リスク継続を支持**するが、**今回新たな原油設備の被害・ヤンブー出荷停止・タンカー損傷・スポットTCE上昇を確認したものではない**。反証・確認：空港の実運航便数と停止状況、石油積出し実績、海上保険・運賃・企業TCEの独立した推移。出典：[Reuters](https://www.reuters.com/world/middle-east/yemens-houthis-renew-warning-against-using-riyadh-airport-2026-10-24/)／[Arab News](https://www.arabnews.pk/saudi-arabia/riyadhs-king-khalid-international-airport-to-reopen-terminals-on-sunday-3005184)。

Brent–WTIは**同限月・同UTC時刻bid/ask未取得につき裁定・縮小未判定**、ロシア産軽油の**米国荷揚げ・価格影響は未判定**、海運利益・AI信用からSOXへの因果は**未判定**を維持。トウモロコシの長期清算値は**データ未取得・未判定**で、単日の価格差から研究結果を推測しない。

## 2026-10-25 15:49 JST：TD3Cベンチマークの代表性という新しい測定仮説（元の表・判定を維持）
[今回の定点レビュー](../daily/2026-10-25-review-1549-jst.md)と[詳細ノート](../topics/2026-10-25-td3c-benchmark-litigation.md)に**「ホルムズ航行制限下ではTD3Cの公表査定が実成約条件や実現TCEを代表しにくいのではないか」**という計測上の競合仮説を追加。**判定：市場参加者の異議・係争の存在は支持、指数の実際の歪み・違法性は未判定**。Mercuriaの主張・Balticの反論・2026/03/25 TD34試行の一次資料・2026/10/21の請求変更報道を区別。**反証：** 船型・積地・保険・時刻・成約可能性を合わせた実成約とTD3Cの差が持続的に小さい。**次の指標：** 通航・fixture、同一路線の実現TCE、TD3C/TD34それぞれの方法論と10/26予定の司法手続。**既存の海運収益仮説は変更せず、追加の10月確定利益も未判定。**

**その他の仮説も最終判定は変化なし**：Brent–WTI（12月限同一UTC時刻の両脚bid/ask未取得）、中東実供給減、ロシア軽油米国荷揚げ、AI信用→半導体は未判定。**トウモロコシ12月限−翌3月限保管キャリー：データ未取得・未判定**。元の単日値を20営業日先の研究成果に流用しない。

## 2026-10-25 19:47 JST 定点照合（元仮説を維持）
[19:47レビュー](../daily/2026-10-25-review-1947-jst.md)：**Reuters 10/25 07:39 UTC（16:39 JST）**によれば、サウジTASIは**場中−2.6%**、Saudi Aramco株**−1.1%**、エジプトEGX30**−2.5%**。**日曜に取引された中東株の市場反応**であり、日足終値・石油供給損害・原油先物再開後の反応を意味しない。Reuters/APの10/25更新で、サウジ側は南部方面の追加弾道ミサイル10発等の迎撃を発表、リヤド空港ターミナル1・2の**再開実績**が報じられた（11:52の再開予定から進展）。安全保障リスクへの警戒と中東株安は確認。ただし**供給実績・持続的リスクプレミアムは未判定**。反証：実出荷量が維持され、原油・保険プレミアムが縮小／指数下落の別要因が優勢。Brent–WTIは**同2026年12月限・同一UTC時刻のbid/ask未取得につき輸出裁定未判定**、TD3Cは係争中で実成約・実現TCE／日本海運会社増益は**未判定**、ロシア軽油の米国実荷揚げ・AI信用→半導体の因果も**未判定**。トウモロコシの複数年度限月別履歴は**データ未取得・未判定**。元の判定表・旧レビューは保持。出典と次の確認点はリンク先。

## 2026-10-25 23:45 JST：日曜中東株の終値を確定（元の仮説・旧場中値は保持）
[23:45定点レビュー](../daily/2026-10-25-review-2345-jst.md)に、**前回19:47ノートの場中値とは別**に、Reutersが10/25取引日の最終値として記載した**サウジTASI −2.7%・Saudi Aramco −0.9%・エジプトEGX30 −3.6%・カタールQSI +0.1%**を記録。サウジは場中最大−3.4%の後に一部回復。Reuters記事の**初報時刻07:39 UTCと記事内の後刻確定終値を同一視せず**、更新後記事を当方が**23:45 JSTに閲覧**した事実を区別する。**中東地域株の下落は確認**、安全保障要因の寄与率・原油の実供給減は**未判定**。反証／競合：他要因調整後に地政学要因の説明力が消える／輸出量維持と輸送プレミアム低下。出典：[Reuters 10/25（更新後の終値記載）](https://www.reuters.com/world/middle-east/gulf-bourses-slip-houthi-saudi-clashes-rattle-investors-2026-10-25/)。

**その他は判定維持**：Brent–WTI同2026/12月限は同一UTC時刻の取引可能bid/ask**未取得・未判定**、タンカーの実現TCE・日本海運会社の追加増益**未判定**、ロシア軽油米国荷揚げ・価格効果**未判定**、AI信用→半導体株の因果**未判定**、トウモロコシ12月限−翌3月限保管キャリーは複数年度の個別限月清算履歴の**データ未取得・未判定**。旧記録を上書きしない。

## 2026-10-26 03:43 JST：中東地域の原油物量回復という反証材料（元仮説・旧判定は保持）

[今回の定点レビュー](../daily/2026-10-26-review-0343-jst.md)および[物量対リスクプレミアムの検証ノート](../topics/2026-10-26-physical-flows-vs-war-risk-premium.md)を追記。**今回新たに照合したのは既報の2026/10/21〜22資料であり、10/26の新規取引・統計ではない。** Reuters 10/22論説が引用したKpler推計：中東石油輸出の10月（10/22時点まで）平均**17.3百万bpd**、9月**16.4**、戦前1〜2月平均**16.9**。同じ10月のホルムズ通航**11.7百万bpd（戦前の約82%）**、サウジYanbu紅海港の輸出**約3.0百万bpd**。JODI公式の**対象2026年8月**サウジ原油輸出は前月比**+0.326百万bpd**、Reuters 10/21による水準**4.451百万bpd**。

**仮説判定の精緻化**：安全保障リスクの存在は支持。一方、**「地域輸出の物量がずっと戦前を大きく下回る」という強い仮説は10/22以前の物量推計に反証方向**。**10/24〜25攻撃後の輸出減は未判定**。価格高騰は輸送費・供給途絶リスクの織り込みと両立しうるが、各要因の因果寄与は未判定。**海運企業の追加の実現利益**、Brent–WTIの同時刻輸出裁定、ロシア軽油の米国荷揚げ、AI信用→SOXはいずれも**未判定**、トウモロコシ保管キャリーは**データ未取得・未判定**を維持。

**反証・次の確認**：10/25後のKpler同一定義推計とYanbu出荷、同一UTC時刻のBrent/WTI 2026年12月限bid/ask、実成約とTD3C・TCE、サウジの月次JODI実績（公表ラグ）、同一ベンダー信用スプレッド。2026/10/22 Reuters論説：[原油物量と物流費](https://www.reuters.com/commentary/reuters-open-interest/dont-mistake-mideast-oil-rebound-normality-2026-10-22/)；[JODI公式](https://www.jodidata.org/)；[Reuters 10/21 JODI数値](https://www.reuters.com/business/energy/saudi-crude-oil-exports-hit-five-month-high-august-data-shows-2026-10-21/)。有料の原データは収録していない。

## 2026-10-26 07:44 JST：取引時間の一次資料確認（市場判定は変化なし）
[当回レビュー](../daily/2026-10-26-review-0744-jst.md)に、[ICE Brent公式取引時間](https://www.ice.com/products/219/Brent-Crude-Futures)および[ICE Brent/WTI上場スプレッド公式仕様](https://www.ice.com/products/1242/specs)の**日曜23:00ロンドン時間開始＝2026/10/26 08:00 JST**（英国10/25冬時間移行後）、[CME WTI公式](https://www.cmegroup.com/education/courses/event-contracts-underlying-markets/wti-overview)の日曜17:00米中部時間開始＝**07:00 JST**を記録。**07:44 JSTはICE Brent取引開始前**で、両脚の同一UTC時刻の約定可能bid/askが存在するとは扱わない。10/23同12月限の**$13.45/bblは異なる市場の別清算時点の算術差**という旧注意を保持。**Brent–WTI裁定未判定、その他の市場仮説も判定変更なし**。中東輸出は10/22以前の推計を10/25以降の実測と混同しない。タンカーの実現利益、ロシア軽油の米国荷揚げ、AI信用→SOXの因果はいずれも未判定。**トウモロコシの保管キャリーはデータ未取得・未判定**。反証条件と次の取得項目はレビューを参照。


## 2026-10-26 11:52 JST 定点照合（元仮説と過去観測は保持）
[今回のレビュー](../daily/2026-10-26-review-1152-jst.md)、[供給網強靱化ノート](../topics/2026-10-26-saudi-singapore-storage-resilience.md)。

- **原油価格・Brent–WTI**：Reuters **10/26 02:32 UTC**の場中報道はBrent **$114.60**・米原油先物 **$101.13**、いずれも10/23終値から下落。WSJ **10/26 02:11 UTC**のLSEG参考値は**2026年12月限Brent $115.01／WTI $101.49（算術差$13.52）**。**両脚の同一UTC秒のbid/askなし**、10/23の清算値差$13.45との水準差を「輸出裁定による拡大・縮小」と結論づけない。**裁定仮説は未判定**。[Reuters](https://www.reuters.com/business/energy/oil-prices-down-almost-1-early-trading-2026-10-25/)／[WSJ](https://www.wsj.com/finance/commodities-futures/oil-declines-on-likely-technical-correction-ad4be59e)。反証条件は、品質・輸送・保険コスト調整後も輸出増で差が縮小しないこと。
- **中東供給リスク／備蓄政策**：Reuters **10/26 01:47 UTC**で、サウジ原油のシンガポール貯蔵を**2027年下期から**開始する**意向表明とMOU署名予定**を確認。**危機への供給網分散の動きは部分的支持**だが、**MOU締結完了・現物入庫・10/25以降のサウジ実供給減は未判定**。反証：計画未実施、在庫前置きが実際に途絶耐性を改善しない。[Reuters](https://www.reuters.com/business/energy/saudi-arabia-store-crude-oil-singapore-second-half-2027-2026-10-26/)。
- **タンカー運賃・海運企業利益**：TD3C審理の予定は**実施・裁判所判断の確認前**。実成約TCE・船種/契約別の収益増は**未判定**。反証：指数が上昇しても実成約TCE・利益が伸びない。
- **ロシア産軽油**：実際の米国荷揚げ・米ULSDクラック下落との因果は**未判定・新規確認なし**。反証：入港しない、輸入後も同条件調整後にULSD低下が生じない。
- **AI信用・金融サイバー（区別）**：Reuters **10/26 01:48 UTC**で、GMO InternetのFXサービス不正アクセスをめぐる補償方針と**同日東京午前の同社株約11%下落（場中）**を確認。**個別事業者のオペレーショナルリスク事例を支持**するが、**AIによる攻撃の直接立証、銀行システム危機、AI企業CDS拡大、SOXへの因果はいずれも未判定**。反証：単独事象にとどまり銀行間決済・預金流出・同年限信用スプレッドへの連鎖がない。[Reuters](https://www.reuters.com/business/finance/japan-companies-compensate-users-cyberattacks-buffet-economy-2026-10-26/)。
- **トウモロコシ12月−翌3月限保管キャリー**：複数作物年度の合法的な個別限月清算値履歴と当時公表済み保管費用・在庫・金利がないため、**データ未取得・未判定**を維持。10/23単日差-14.25¢/buは予測利益ではない。


## 2026-10-26 15:50 JST 定点照合（元仮説・旧判定は保持）
[当回レビュー](../daily/2026-10-26-review-1550-jst.md)を追記。Reuters **10/26 03:48 UTC**で、フーシ派によるサウジ東西パイプラインのポンプ場・リヤド空港への**新たな攻撃主張**を確認。ただし**サウジ側の同攻撃の即時確認なし**で、命中・損傷・操業停止・原油純供給減は**未判定**。攻撃主張の存在は安全保障リスク継続と整合、10/22までのKpler物量回復推計とは時点が違う。**反証／確認**：Saudi Aramco・政府の操業発表、Yanbuでの後続積出し、同一定義の船舶輸送量、保険料。[Reuters](https://www.reuters.com/world/middle-east/houthis-say-they-attacked-east-west-oil-pumping-stations-no-saudi-confirmation-2026-10-26/)。

Reuters **10/26 02:49 UTC**でIEA事務局長が2027年も戦前水準への正常化を想定しないとの**見解**と冬季軽油需要・製油所定修への警戒を表明。[Reuters](https://www.reuters.com/business/energy/ieas-birol-does-not-expect-energy-markets-return-pre-war-levels-2027-2026-10-26/)。これは10/26実物供給量を測定した新値ではない。原油の10/26 **04:26 UTC場中** Reuters報道値はBrent $114.51、WTI $101.04（いずれも下落）。**同12月限の同一UTC秒bid/askがないため輸出裁定は未判定**。ロシア産軽油の米実荷揚げ・ULSD価格因果、タンカー実成約TCEと海運3社の追加実現利益、AI信用→SOXの因果も**未判定**を維持。Mercuria–Balticの10/26審理結果は未確認。**トウモロコシ保管キャリーはデータ未取得・未判定**、単日差-14.25¢/buを検証成果としない。


## 2026-10-26 19:52 JST 定点照合（原仮説・既往判定は保持）
[当回レビュー](../daily/2026-10-26-review-1952-jst.md)／[海運ノート追記](../topics/2026-10-24-global-vs-japan-shipping-middle-east.md)。

- **2026/10/23に事前記録した10/26川崎汽船の同業比上昇**：10/26東証15:30終値で川崎汽船**3,412円・+2.59%**、商船三井**7,382円・+2.43%**、日本郵船**7,266円・+1.92%**。川崎は同業2社単純平均を**+0.41ポイント**上回り、**当日相対上昇という限定仮説を支持**。ただし10/26高値**3,449円**は事前の3,450円超シナリオを満たさず、10/23夜PTSの3,415円も終値では上回らない。**原因・再現性は未判定**。反証・留保：市場調整後の超過収益が消える、翌営業日以降に反転。出典：[Traders Web 9107](https://www.traders.co.jp/stocks/61_9107/historical)・[9104](https://www.traders.co.jp/stocks/61_9104/historical)・[9101](https://www.traders.co.jp/stocks/61_9101/historical)（**取引日10/26、照合19:52 JST**）。
- **輸送費・netback**：[WSJ 10/26 08:51 GMT](https://www.wsj.com/finance/commodities-futures/oil-declines-on-likely-technical-correction-ad4be59e)がRystad推計の**Yanbu→Ningbo運送コスト（対象10/22 $48/bbl、9月初め $24/bbl）**を報道。**輸送摩擦の存在は支持方向**、特定船主の実成約TCE・日本3社確定増益とサウジ輸出者の実現netbackは**未判定**。反証：同航路の成約・費用負担条件で水準が再現しない／高運賃でも実現TCE・利益が伸びない。
- **外交と場中市場反応**：[Reuters 10/26 08:28 UTC](https://www.reuters.com/world/middle-east/middle-east-markets-rebound-diplomacy-fuels-hopes-easing-iran-hostilities-2026-10-26/)ではサウジTASI**場中+2.5%**・Aramco**+1.3%**、カタールQSI**+1.8%**、エジプトEGX30**+0.6%**。テヘラン高官協議と仲介報道は**緊張緩和期待という競合仮説の支持方向**、停戦・合意・25日以降の実物供給回復は**未判定**。反証：協議破綻、追加攻撃・通航制約持続、終値や輸出量が改善しない。[Reuters外交10/26 03:20 UTC](https://www.reuters.com/world/asia-pacific/top-officials-mecca-pact-countries-meet-iranian-officials-tehran-monday-two-2026-10-26/)。
- **Brent–WTI**：Reuters **10/26 09:59 UTC場中**でBrent**$114.82**、米WTI**$101.19**（それぞれ前営業日比-1.63%、-2.00%）だが、**同2026/12月限・同一UTC秒bid/ask未確認につき裁定／縮小は未判定**。出典：[Reuters更新市況](https://www.reuters.com/business/energy/oil-prices-down-almost-1-early-trading-2026-10-25/)。
- **ロシア軽油→米ULSD／AI信用→半導体**：新規の米国実荷揚げ、同年限同ベンダー信用系列とSOXの検証を得られず、**因果は未判定**。**コーン12月−翌3月保管キャリー**：所定の個別限月複数年度CSV `research/corn-dec-mar/data/input/futures_daily.csv` は今回取得できず**データ未取得・未判定**。単日カーブの-14.25¢/buから統計結果を作らない。

## 2026-10-26 23:52 JST：ロシア軽油の供給余力と米国受渡を区別（元仮説を保持）

[23:52 定点レビュー](../daily/2026-10-26-review-2352-jst.md)／[ロシア軽油：出荷までの段階別検証](../topics/2026-10-26-russian-diesel-output-quota-vs-us-arrival.md)。

- **新事実・観測時点**：[Reuters 10/26 12:59 UTC](https://www.reuters.com/business/energy/russian-refiners-ramp-up-diesel-output-after-us-deal-sources-say-2026-10-26/)の業界関係者推計：ロシア軽油日産は9月約17.5万トン、10月上旬約16万トン、中旬以降約18万トンに向けて回復。季節需要約14万トン/日との差約4万トン/日は潜在的な輸出余力で、実船積・米国荷揚げ・価格低下ではない。Reuters報道の10/23 NY向けAISも着岸実績ではない。**供給回復方向は部分支持、米国のULSD価格効果は未判定**。反証：生産確報／港湾積出・通関が追随しない、または到着後のULSDやクラックが需給統制後に低下しない。
- **中東輸送**：[Reuters 10/26 10:24 UTC](https://www.reuters.com/world/middle-east/how-houthi-attacks-have-grounded-flights-across-saudi-arabia-2026-10-26/)のCirium集計は10/8〜25にリヤド空港で4,071/4,736便が欠航（86%）。**航空の実障害は支持**、Yanbu原油輸出停止・海運運賃・日本船社の確定増益は**未判定**。反証：実際の港湾稼働・東西パイプライン流量・船舶成約が供給減を裏付けない。
- **AI信用**：[Reuters 10/26 13:41 UTC](https://www.reuters.com/business/hsbc-cuts-global-equities-neutral-middle-east-ai-risks-2026-10-26/)のHSBC世界株評価引下げはリスク認識の表明。**同一銘柄・同一商品・同一年限のCDS/OAS改善悪化を示さず、SOX因果は未判定**。反証：信用スプレッドに一貫した超過拡大・先行性がない。
- **Brent–WTI／タンカー／日本海運**：2026年12月限の両建て同期bid/ask、追加実成約TCE・部門確報なし。前回の条件付き支持と**裁定・確定利益未判定**を維持。TD3C係争の新たな裁判所判断は確認できていない。
- **トウモロコシ12月限−翌3月限**：実測複数年清算値入力がリポジトリに存在しない（10/26点検）。**データ未取得・未判定**。反証：時点依存キャリーとコスト考慮後、20営業日後の年度外予測が再現しない。単日のカーブを戦略成果として扱わない。

**検証の原則**：各資料の公表日時と参照期間、取引時点を分離。過去の仮説・数値・反証条件は改変しない。有料時系列と秘密情報は転載しない。

## 2026-10-27 03:43 JST 定点照合（原仮説と既往結果は変更しない）
[今回の定点レビュー](../daily/2026-10-27-review-0343-jst.md)／[Meta資本政策と信用の違い](../topics/2026-10-27-meta-equity-issuance-vs-ai-credit.md)／[原油・SPR・エジプト](../topics/2026-10-27-intraday-oil-rebound-spr-egypt.md)。
- **価格更新**：[Reuters 10/26 16:37 UTC](https://www.reuters.com/business/energy/oil-prices-down-almost-1-early-trading-2026-10-25/)はBrent **$117.21（+0.4%）**／WTI **$102.92（−0.34%）**という**場中参考値**。10/26午前の両銘柄下落からBrentは前日比プラスとなったが、両脚**同2026/12月限・同一UTC秒の執行可能bid/askを得ていない**。輸出裁定縮小は**未判定**。反証：湾岸価格・運賃補正後もスプレッドが縮まらず米国輸出も増えない。
- **米SPR**：[Reuters 10/26 15:21 UTC](https://www.reuters.com/business/energy/oil-stocks-us-strategic-petroleum-reserve-fall-lowest-level-since-1982-2026-10-26/)がDOEの**10/23週末282.6百万bbl**を報道。緊急供給余力低下の観測であり**中東実輸出減少を示さない**。[DOE 10/23公表](https://www.energy.gov/articles/energy-department-authorizes-strategic-petroleum-reserve-exchange-support-fuel-supply)の40万bbl緊急交換は**承認**。反証・次の確認：SPR週次残高、10/25以降Yanbu実輸出と稼働、タンカー積出し。中東原油の新たな純供給減は**未判定**。
- **中東政治**：[Reuters 10/26 13:08 UTC](https://www.reuters.com/world/middle-east/egypt-approves-military-support-saudi-arabia-after-houthi-attacks-escalate-2026-10-26/)のエジプト議会の防衛支援権限付与は**支持（決議の存在）**、派兵・Bab el-Mandebの通航回復は**未判定**。反証：正式な派兵要請・海上護衛・通航改善が確認できない。
- **MetaとAI信用**：[Meta公式 10/26](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx)で**350億ドル公募（225億ドル普通株フォワード＋125億ドル強制転換優先預託証券）開始、将来最大600億ドルATM構想**。前者の全額現金即時受領でも後者の実行でもない。**資金調達需要の存在は支持**、同条件CDS/OAS悪化とSOXへの因果は**未判定**。反証：実調達・信用価格の超過悪化・半導体株の先行予測効果が出ない。
- **タンカー／国内海運**：実成約・契約別TCE・10月以降の事業利益の確定新値なし、**未判定**。**ロシア軽油**：前回の生産回復方向部分支持を保持し米荷揚げとULSD影響は**未判定**。**トウモロコシ保管キャリー：データ未取得・未判定**。ライセンス付生価格や秘密情報を転載しない。


## 2026-10-27 07:44 JST 定点照合（元の仮説・過去の判定を保持）
[07:44レビュー](../daily/2026-10-27-review-0744-jst.md)／[Anthropic向けSPVの信用リスク](../topics/2026-10-27-anthropic-broadcom-spv-ai-credit.md)。
- **Brent–WTI**：10/26の**12月限**報道終値はICE Brent $115.81、NYMEX WTI $101.76（[Reuters 10/26終値](https://www.reuters.com/business/energy/oil-prices-down-almost-1-early-trading-2026-10-25/)、[WSJ 10/26 19:55 UTC](https://www.wsj.com/finance/commodities-futures/oil-declines-on-likely-technical-correction-ad4be59e)）、**非同期清算値の算術差は$14.05**。10/23同算術差$13.45との違いを**裁定スプレッド実際の拡大とは断定しない**。ICE Brent **2027/01 $110.74**とも混同禁止。**同一UTC秒bid/ask未取得・輸出裁定未判定**。反証：運賃/品質調整後に輸出が増えず縮小が見られない。
- **中東安全保障・原油純供給減／海運利益**：[UKMTOを引用した10/26報道](https://h.aa.com.tr/en/middle-east/vessel-reported-on-fire-off-iraq-s-al-faw-uk-maritime-agency/4101675)でAl-Faw南東約63海里の船舶火災の**第三者通報**（原因・船舶・損傷未確認）。安全航行リスクの継続は支持方向、**実原油積出減・実成約TCE・海運会社増益は未判定**。反証：船名/IMO・UKMTO確報/港湾流量で損傷や供給減が裏付けられない、実現TCEがコスト増で相殺。10/20の約30海里の事例とは別件。
- **AI信用と半導体株**：[Broadcom・金融4社10/26公式](https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce)はAnthropicへの機器リースのための**630億ドルSPV融資構造**を公表（[Reuters 10/26 20:32 UTC](https://www.reuters.com/legal/transactional/wall-street-banks-blackstone-line-up-63-billion-finance-broadcom-chips-anthropic-2026-10-26/)）。第一順位組成、第二順位コミット、Broadcomによる残価サポートは**資金調達・残価リスク経路の存在を支持**するが融資全額実行/損失/信用プレミアム拡大は未確認。10/26引け[Reuters](https://www.reuters.com/business/us-stock-futures-edge-up-oil-falls-heading-into-earnings-barrage-2026-10-26/)では**SOX +2.8%・Meta -1.9%**。単純な同日一律下落仮説は支持されず、**CDS/OASからSOXへの因果は未判定**。反証：同一定義信用指標の拡大・株式先行効果が統制後に再現しない。
- **ロシア産軽油**：10/26生産回復方向は既存部分支持を維持。米国**着岸・荷揚げ/通関、ULSD価格因果は未判定**。反証：予定船が実際に荷揚げしない／米製品価格・クラックが需給統制後も下がらない。
- **コーン12月限−翌3月限**：複数作物年度の個別限月清算値CSVは**データ未取得・未判定**。反証：保管キャリー超過と20営業日後の価格差変化が年度外・コスト控除後に再現しない。


## 2026-10-27 11:48 JST 定点照合（元仮説と旧判定は保持）

[11:48レビュー](../daily/2026-10-27-review-1148-jst.md)。**新たな中東迎撃報告と、AI需要縮小の条件付きシナリオ**を追記した。事前に定めた検証条件は変更しない。
- **中東**：[Reuters 10/27 02:17 UTC](https://www.reuters.com/world/middle-east/saudi-led-coalition-says-it-intercepted-houthi-missiles-drones-attacking-kingdom-2026-10-27/)で、連合が東部向け弾道ミサイル3発・南部向けドローン4機の迎撃を発表。**安全保障リスク継続を支持**、命中/施設損傷/Yanbu積出減による原油純供給減は**未判定**。反証・確認：Aramco操業・港湾実荷動き・損害の公式確報。
- **10/27原油**：[Reuters 00:37 UTC公表、価格観測00:00 UTC](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)のBrent $115.15/WTI $101.32は**新しい取引日の場中価格**。同2026/12限・同一UTC秒のbid/askとは確認できず**Brent–WTI輸出裁定は未判定**。反証：輸送/品質差を引いても実際の裁定による米国輸出増・差の縮小が起きない。
- **AI・半導体**：[Reuters 10/27 02:17 UTC](https://www.reuters.com/world/asia-pacific/bank-korea-warns-countrys-chip-exports-could-fall-by-up-100-billion-if-ai-2026-10-27/)はBOKの**悲観シナリオ**（2027年輸出が従来見通し比500億～1000億ドル減、韓国半導体単価10%低下の仮定、GDP成長率約0.4pt押し下げ）を引用。**実現予測値ではない**。[Reuters 01:46 UTC](https://www.reuters.com/world/china/global-markets-global-markets-2026-10-27/)の**日経平均+1.9%、KOSPI+4%超は場中値**。信用スプレッド実績および信用→SOX/日本半導体株の因果は**未判定**。反証：同条件OAS/CDSに悪化がなく、株式への先行性も標本外で再現しない。
- **タンカー海運・ロシア軽油**：新たな実成約TCE・日系3社確定セグメント利益／米国軽油荷揚げ・ULSDの需給調整済価格影響は未確認で**未判定**。先行するロシア生産回復の部分支持は維持。反証：高運賃でも運航費・稼働日数のため実利益増がない／ロシア軽油が入港しないか米国内価格効果がない。
- **コーン12月−翌3月キャリー**：GitHub APIで`research/corn-dec-mar/data/input/futures_daily.csv`は404。**データ未取得・未判定**。単日気配から統計・利益を推測しない。反証：年度外・時点依存キャリー・取引費用調整後に予測効果がない。

## 2026-10-27 15:45 JST 定点照合（既存仮説・観測は保持）
[15:45レビュー](../daily/2026-10-27-review-1545-jst.md)。Reutersの10/27場中価格**04:18 UTC**はBrent $114.81 / WTI $100.88。両市場の2026/12限・同時刻bid/askではないため**Brent–WTI裁定未判定**。同記事内の**ANZ分析**は湾岸原油輸出4週続落・ホルムズ通常比約60%・中間留分在庫5年平均比約−5%とするが、**ANZ原資料/比較定義/対象週は未確認**。先行Kplerの「10/22時点までの10月中東地域輸出月途中平均回復・海峡約82%」と**別系列**として保持し、実際のサウジ被害・純輸出減・海運増益は**未判定**。反証は同一定義の最新の通航・出荷増、保険/実成約TCEの正常化。

**AI信用**：[Reuters 10/27 06:08 UTC](https://www.reuters.com/technology/nvidia-meta-partner-muse-agent-nvidia-invests-3-billion-2026-10-27/)でNVIDIAはMetaの株式公募に**$3bn投資する意向**、Muse協業拡大を発表。既存のMeta 10/26資料の半導体供給企業合計最大$5bnの購入意向に**単純加算しない**。払い込みやCDS/OAS、SOXへの因果は**未判定**。反証は同一条件信用スプレッドの悪化・株価先行予測が再現しないこと。**ロシア軽油の米荷揚げと価格影響、日系海運会社の実現利益は未判定**。**トウモロコシ保管キャリーはデータ未取得・未判定**。


## 2026-10-27 19:52 JST 定点照合（元仮説・過去の値は保持）
[19:52レビュー](../daily/2026-10-27-review-1952-jst.md)を追記。新たな証拠による**条件付きの更新のみ**。価格の観測時間、報道の公開時刻、統計対象窓を区別する。

- **Brent–WTI**：[Reuters 10/27 09:18 GMT時点](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)でBrent **$116.26**（+0.39%）、WTI **$102.16**（+0.39%）。04:18 UTC時点の$114.81/$100.88から場中反発。**同2026年12月限・同一UTC秒bid/ask未取得、執行可能裁定・縮小は未判定**。反証：品質・費用を補正した純裁定余地/米輸出増/持続縮小が生じない。
- **中東実物流**：[WSJ 10/27 09:10 GMT、Kpler引用](https://www.wsj.com/finance/commodities-futures/oil-falls-amid-diplomatic-efforts-to-ease-u-s-iran-hostilities-c235ed0a)。**海峡直近7日平均9.34百万b/d（戦前17.15、約54%）**と、**イランを除く中東原油の10月ここまでの海外供給16.7百万b/d（戦前16.3）**は対象/期間/経路が異なる。**海峡輸送制約支持、広域原油追加純供給減は未判定**。10/22 Kpler 11.7百万b/d/82%やANZ 60%と連結不可。反証：同一定義の積出量が正常化、または通航減でも輸出総量・着荷量が維持される。
- **タンカー／TD3C**：[Lloyd's List 10/26](https://www.lloydslist.com/LL1158818/Trial-evidence-highlights-TD3C-scepticism--even-inside-Baltic-Exchange)でMercuria–Baltic訴訟の**実際の審理開始**と、原告の内部証言引用を確認。ただし**司法判断・指数の虚偽認定ではない**。実成約TCE・日本3社の増益は**未判定**。反証：指数が同契約・航路で実成約の代表性を保つ／高運賃でも保険費・不稼働で実現利益が増えない。
- **ロシア軽油**：[FT 10/27付（有料記事）](https://www.ft.com/content/d847744f-cfa5-4dc5-bdd2-faeee0b584f7)は**3隻約14万tの11月米港到着予定、うち制裁関係の船を含む**と報道。FT本文詳細、IMO・制裁名簿・AIS・米通関は独立未照合。**到着予定≠米荷揚げ≠ULSD下落**。生産回復は既存の部分的支持を維持、価格効果は未判定。反証：入港/荷揚げがなく、または米製品価格に需給調整後の下落なし。
- **AI信用**：[Reuters 10/26 20:32 UTC](https://www.reuters.com/legal/transactional/wall-street-banks-blackstone-line-up-63-billion-finance-broadcom-chips-anthropic-2026-10-26/)はAnthropic向け$63bn SPVの第一順位を**関係者2人による約$43.5bn推計**と報道。[10/26公式](https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce)はトランシェ額を開示していない。**信用条件・残価負担構造の追加資料、CDS/OAS拡大とSOXへの因果は未判定**。反証：信用スプレッドの同年限超過拡大・先行性を検出できない。
- **トウモロコシ12月−翌3月限**：10/27 GitHub APIで研究入力CSV 404、複数年度個別限月履歴なし。**データ未取得・未判定**。反証：年度外・情報時点整合・保管/金利/基差/売買費用控除の予測力がない。ライセンス生データ・秘密鍵なし。


## 2026-10-27 23:50 JST 定点照合（元の仮説と旧観測は保持）
[23:50レビュー](../daily/2026-10-27-review-2350-jst.md)を追加した。前回19:52確認以降の新規報道の公表時刻と価格観測時刻は分けて扱う。
- **中東・原油の実物流**：[Reuters 10/27 11:06 UTC](https://www.reuters.com/business/energy/yemens-houthis-say-they-launched-an-attack-saudi-ras-tanura-oil-refinery-2026-10-27/)はフーシ派のRas Tanura製油所へのミサイル攻撃・火災の**主張**を報じ、**サウジ未確認**。Bloomberg関係者情報による火災鎮圧報道もあり、稼働・港湾積出減は確認されない。製油能力55万b/dは被害や輸出減の量ではない。**安全保障リスク継続を支持、追加原油純供給減は未判定**。反証：公式被害報告・積出しデータが停止を裏付けず、実物フローが維持される。
- **原油場中値／Brent–WTI**：[Reuters 10/27（価格観測13:11 GMT、22:11 JST）](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)のBrent $114.81/WTI $100.98は19:52レビューの09:18 GMT観測$116.26/$102.16から再反落。**12月限の同期両サイド気配ではなく、縮小裁定は未判定**。反証：品質・航路コスト調整後の米輸出裁定余地と輸出増・スプレッド縮小が観測されない。
- **AI信用**：[Reuters 10/27 14:33 UTC](https://www.reuters.com/business/finance/neocloud-firm-argentum-ai-talks-5-billion-ai-chip-financing-sources-say-2026-10-27/)はArgentum AIが非投資適格顧客にリースするチップのための**50億ドル規模の資金調達を交渉中**と報道。**交渉・契約売上120億ドル超という関係者談は実融資や信用損失ではない**。信用力別の資金調達リスク経路は仮説を具体化するが、OAS/CDS悪化とSOX下押しの因果は**未判定**。反証：交渉不成立、信用補完によるリスク除去、同条件スプレッドと株価の予測力なし。[Argentumノート](../topics/2026-10-27-argentum-neocloud-credit.md)。
- **海運増益・ロシア軽油**：実成約fixture/TCE・国内船社の確定増益と、11月予定便の米実荷揚げ／米ULSD価格効果に新たな確報なく**未判定**（ロシア生産回復の既存部分的支持は維持）。**トウモロコシ12月限−翌3月限キャリーはCSV未取得のため「データ未取得・未判定」**。

## 2026-10-28 03:47 JST 定点照合（元仮説・過去の観測は維持）

[03:47レビュー](../daily/2026-10-28-review-0347-jst.md)／[AI借換え・ECB信用ノート](../topics/2026-10-28-ai-credit-refinancing-moodys-ecb.md)を新規追加。新規情報の**公表時刻、観測時刻、統計対象期間を区別**する。

- **原油とBrent–WTI**：[Reuters 10/27更新記事・場中観測17:44 UTC](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)はBrent $113.72/WTI $99.83（前日比−1.8%/−1.9%）。13:11 UTCの$114.81/$100.98から下落。**10/27の確定清算値ではない**、かつ**同2026年12月限・同一UTC時刻bid/askなし**。縮小裁定**未判定**。反証：費用・品質調整後の純裁定が持続せず米輸出量・差の縮小で裏付けられない。
- **ロシア軽油／原油**：[Reuters 10/27 16:43 UTC](https://www.reuters.com/business/energy/russia-oil-exports-through-western-ports-forecast-fall-november-traders-say-2026-10-27/)は**11月のロシア西部港の原油（カザフスタン原油通過分含む）海上輸出が前月比0.1〜0.2百万b/d減りうるという関係者予測**。別の関係者談による10月後半の精製処理の前半比約25%増は**精製の回復を部分的に支持**するが軽油生産率・米荷揚げ実績ではない。原油輸出量の見込みと製品輸出実績を混同しない。**11月輸出予測の実現・米ULSD価格効果は未判定**。反証：計画更新で減少せず、11月船舶が荷揚げせず、需給を統制しても軽油価格効果なし。
- **AI信用**：[Reuters 10/27 14:49 UTC](https://www.reuters.com/legal/transactional/ai-financing-driving-private-credit-growth-refinancing-risks-rise-moodys-says-2026-10-27/)のMoody's Ratings分析は**2027–29年の借換え集中リスク**、2027年ハイパースケーラー5社＋CoreWeaveの設備投資**約1兆ドルの予測**を提示。**PIK利用17%はMoody's追跡607借り手の母集団の数字**で、AI限定とみなさない。[Reuters 10/27 07:00 UTCの意見コラム](https://www.reuters.com/commentary/reuters-open-interest/ai-tremor-exposes-markets-volatility-fault-lines-2026-10-27/)が引用するBarclays推計は**AI関連信用銘柄間のスプレッド格差約65bp**（最近約3倍）。原資料未取得の二次分析につき、**信用条件の階層化は暫定的部分支持**、市場全体のOAS悪化や**信用→SOX因果は未判定**。反証：年限・格付け・流動性等統制後に差が消え、標本外で信用スプレッドに先行予測力がない。
- **ECB銀行融資（AIの一次資料）**：[ECB 10/27公表、調査09/21～10/06・対象2026Q3・159行](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr261027~506ef03145.en.html)では、**全企業向け**貸出基準ネット9%引締め、銀行の大半はAI専用の定量審査基準を未導入。AIインフラ向け融資需要の増加は予想であり実行済額ではない。**AI信用事故・SOX波及は未判定**。反証：独立の与信条件悪化、借換え費用増加、同条件企業の超過スプレッドが確認されない。
- **中東実物流・海運利益**：[Reuters 10/27 06:13 UTC](https://www.reuters.com/business/energy/no-pressure-us-cut-russian-oil-imports-indian-oil-minister-says-2026-10-27/)のインド向け中東原油**9月輸入が戦前水準に回復**という観測を補足。ただし**9月着荷≠10月27日Ras Tanura操業・積出確報**。安全保障リスク継続は既存支持、追加原油純供給減・タンカー実成約TCE・日本船社実現利益は**未判定**。反証：同一出典・港別積出維持と運賃低下／高運賃でも保険等控除後TCE・企業利益が増えない。
- **トウモロコシ12月限−翌3月限**：指定の複数作物年度の個別限月清算値`research/corn-dec-mar/data/input/futures_daily.csv`は引き続き404。**データ未取得・未判定**。反証：当時公表データのみによる年度外・保管キャリー超過・取引費用控除後の20営業日予測力が再現しない。実測価格なしに効果・収益を推定しない。


## 2026-10-28 07:43 JST 定点照合（過去の仮説・観測・反証条件は保持）
[07:43レビュー](../daily/2026-10-28-review-0743-jst.md)。新規事実は10/27原油の**引け後報道清算値**、Metaの**価格決定一次資料**、米国株の**引け**。出典のページ表示日と観測対象の市場日を区別する。
- **Brent–WTI**：[WSJ](https://www.wsj.com/world/middle-east/oil-prices-fall-as-traders-assess-iran-diplomacy-saudi-attacks-95bb0210)／[石油市況日報](https://pflpetroleum.com/reports/petroleum-daily-report-10-27-2026/)の同**2026年12月限**の10/27引け後報道清算値はBrent **$113.88**、WTI **$99.90**、差**$13.98/bbl**。前回の17:44 UTC場中観測や10/26清算値とは種類が異なる。ICE/NYMEX**同一UTC秒の執行可能bid/askではない**ため輸出裁定の縮小は**未判定**。反証：費用控除純裁定と米輸出増・同期差縮小が成立しない。
- **AI資金調達**：[Meta公式価格決定](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Pricing-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx)で普通株フォワード公募**$25bn**（当初$22.5bn）、強制転換優先株預託**$12.5bn**、合計**$37.5bnの価格決定**。既存の最大$60bn ATM（未実施）と合わせた$97.5bnを**入金済み**としない。普通株フォワードの当初着金予定なし、10/29受渡は未了。**株式調達経路の存在・具体化を支持、信用スプレッド悪化は未判定**。反証：公募不成立、ATM未実施、同一年限OAS/CDS悪化の予測性なし。
- **米国AI関連株**：[Reuters 10/27米市場引け・16:22 EDT更新](https://ca.marketscreener.com/news/wall-street-ends-higher-on-revived-ai-momentum-ce785cddde81f423)でNasdaq Composite **+1.18%**、半導体株3営業日続伸、Meta **−1.6%**。同日・異なる企業の株価と信用債務価格は別。**AI信用スプレッド→SOX下押し因果は未判定**。反証：信用格差が縮小/統制後に消え、標本外で株価下落の先行予測性なし。
- **中東・タンカー・日本海運**：Ras Tanura 10/27攻撃主張後の当局操業/積出し確報・同一航路fixture/TCE・日系船社利益は今回の追加資料で得られず、**安全保障リスク継続の既存支持**・**追加供給減と実現利益は未判定**。反証：実出荷維持や費用控除後利益改善なし。
- **ロシア産軽油**：11月米港到着予定は既知だが、荷揚げ/通関および米ULSD価格効果の追加確報なし。生産回復の既存部分的支持を維持、**価格効果未判定**。反証：着荷が起こらない、需給調整後に価格波及なし。
- **トウモロコシ12月−翌3月限**：公開遅延画面は歴史的個別限月清算値の代わりにならない。複数年度の清算値CSV未登録につき**データ未取得・未判定**。反証：当時利用可能な条件・保管/金利/基差・費用控除後20営業日OOSで再現性なし。ライセンス付き生データ・鍵は保存しない。


## 2026-10-28 11:51 JST 定点照合（原仮説・過去観測は保持）
[11:51レビュー](../daily/2026-10-28-review-1151-jst.md)／[SK hynix実需とAI信用の分離](../topics/2026-10-28-sk-hynix-ai-demand-vs-credit.md)を追加。
- **原油**：[Reuters 10/28 01:49 UTC記事](https://www.reuters.com/world/asia-pacific/oil-prices-rise-after-attack-saudi-arabian-refinery-reignites-supply-concerns-2026-10-28/)は10/28 01:40 UTC場中Brent **$115.36**、WTI **$101.12**（10/27の報道清算値から反発）。契約限月と同期bid/askは不明なので**Brent–WTI執行可能裁定は未判定**。反証：同12月限同期スプレッドがコスト控除後の米輸出採算を満たさない／輸出増につながらない。
- **中東設備被害**：同記事は10/27 Ras Tanura攻撃のフーシ派主張とサウジ当局による未確認を明示。55万bbl/日は製油能力で**確定減産量ではない**。安全保障リスク継続は既存支持を維持、純原油輸出減・船社実現利益は**未判定**。反証：港湾積出・工場操業が維持、費用控除後の船社TCEが増えない。
- **AI実需要**：[SK hynix公式Q3決算 10/27 19:45 ET](https://www.prnewswire.com/news-releases/sk-hynix-announces-3q26-financial-results-302921407.html)では営業利益**83.3338兆ウォン**、14社とのLTAが2027–28年能力の50%超に相当。**供給側のAI需要の強さは支持**、AI設備借り手の返済力・OAS/CDS改善や**信用→SOX因果は未判定**。反証：将来出荷・売上が継続せず／信用系列の統制後先行性がない。
- **調達先分散**：[Reuters 10/28 01:23 UTC](https://www.reuters.com/business/openai-plans-buy-googles-ai-chips-information-reports-2026-10-28/)のGoogle TPU購入計画は二次情報・未契約。GPU残価/貸付担保への波及**未判定**。反証：実取引・残価価格・担保掛目の変化なし。
- **ロシア軽油・タンカー運賃・日本海運**：11月実荷揚げ、同一航路実成約とTCE、増分部門利益の確報なし。既存の精製回復の部分支持を維持し、米国軽油価格効果・船社増益は**未判定**。
- **トウモロコシ保管キャリー**：複数年度・個別限月清算値CSV未取得につき**データ未取得・未判定**。20営業日後の統計結果や利益を作らない。



## 2026-10-28 15:43 JST：金融政策のエネルギー波及・生産者実益・AI担保残価と個別債券報道（原仮説を維持）

[15:43定点レビュー](../daily/2026-10-28-review-1543-jst.md)／[RBNZとEquinorの因果の切分け](../topics/2026-10-28-energy-inflation-rbnz-equinor.md)／[CXMTとBeignet：品質差・信用価格の切分け](../topics/2026-10-28-cxmt-hbm-and-beignet-credit.md)を追加。
- [RBNZ一次資料、2026-10-28（14:00 NZDT／10:00 JST）](https://www.rbnz.govt.nz/news-and-events/news/2026/10/ocr-held-at-2-75-percent)：OCRを2.75%に4対3で据え置き。CPI2026Q3前年比3.7%は**実績**、2026Q4の4.4%は**燃料価格等を前提とする予測**。原油供給・製品/船舶輸送価格の高騰と、不透明なAI投資融資・長期金利の金融安定リスクに言及。**判定：中東発のコスト波及を中銀が検討する事実を支持。実際の供給量減・将来インフレ実現・AI信用損失は未判定**。反証：事後の価格・期待インフレに二次影響が残らず、金融不安も発生しない。
- [Reuters 2026-10-28 05:49 UTC（14:49 JST）](https://www.reuters.com/business/equinor-profit-jumps-middle-east-war-lifts-oil-gas-prices-2026-10-28/)：Equinorの2026Q3調整後税引前利益$12.34bn（前年同期$6.22bn）、2026年生産伸長見通し約4%へ引上げ。**判定：中東外生産者の高値受益を個社実績で支持。ただし日本タンカー船社の収益性は未判定**。反証：企業部門別で価格ではなく一時的要因等が主要増益理由となる、海運会社の実現TCE・契約別利益が増えない。
- [Reuters 2026-10-28 04:50 UTC（13:50 JST）](https://www.reuters.com/world/china/chinas-cxmt-start-advanced-ai-memory-production-despite-poor-yields-sources-say-2026-10-28/)：CXMTのHBM3E限定量産計画と匿名関係者の歩留まり20～30%・SK hynix約70%推計。**判定：製造品質・競争環境の差を調査する必要性は支持、GPU/AI機器担保残価や信用損失は未判定**。反証：同等機器の再販価格/与信掛目に差が認められない。
- [Barron's 2026-10-28付（価格観測日時未確認）](https://www.barrons.com/articles/meta-platforms-bond-ai-data-center-3094ec88)：Beignet SPVの約$27.3bn債券が額面約$0.92・利回り約7.3%との二次報道。個別CUSIP・時刻・国債金利を未照合。**判定：債券価格の報道を確認／信用OAS拡大と信用→SOX因果は未判定**。反証：同条件の国債・流動性調整後に信用悪化が再現しない。
- [Reuters 2026-10-28（04:35 UTC報道価格観測）](https://www.reuters.com/world/asia-pacific/oil-prices-rise-after-attack-saudi-arabian-refinery-reignites-supply-concerns-2026-10-28/)：API関係者ベースの10/23終了週米原油在庫**−2.03百万bbl**。**公式EIAを未取得**、改訂前民間速報であり確定増減と扱わない。**Brent–WTI同12月限・同UTC秒・bid/askは未取得→裁定未判定**。Ras Tanuraの損傷実績、海運成約、ロシア軽油の11月米荷揚げも未判定。
- **CBOTトウモロコシ12月限−翌3月限：データ未取得・未判定**。研究ディレクトリには研究計画・コード・台帳があるが複数年度の個別限月清算値が無い。推計収益/支持率は一切記載しない。

**次回**：EIA公式在庫vs API速報、Aramco港湾/操業、Baltic実成約TCE、同UTC秒両脚原油気配、Beignetの取引時刻とOAS、半導体量産実績。公表日時・対象期間・限月を分離し、ライセンス付き生データ・秘密鍵を転載しない。


## 2026-10-28 19:52 JST：Clarksea横断収入指数とAI信用・為替の波及経路（旧仮説は保持）

[19:52定点レビュー](../daily/2026-10-28-review-1952-jst.md)／[Clarkseaと日系海運利益の分離](../topics/2026-10-28-clarksea-multi-sector-earnings-vs-japan.md)／[AI信用と為替](../topics/2026-10-28-ai-credit-flows-fx-contagion.md)。
- **海運**：[Cinco Días 2026-10-28 05:30 CET](https://cincodias.elpais.com/mercados-financieros/2026-10-28/las-navieras-se-hacen-de-oro-con-el-alza-de-los-fletes-y-disparan-un-75-el-beneficio-medio-por-barco.html)はClarksea Indexの船種横断加重推計日収入**7.4万ドル超（前年比+75%、10年平均比+92%）**と報道。ただし原系列算出日・加重比を独立未照合。**海運全体の高収入環境は二次報道による支持材料／TD3Cの指数代表性、船主実現TCE、日本郵船/商船三井/川崎汽船の追加利益は未判定**。反証：同条件の成約・稼働日数と費用控除後利益が上昇しない。
- **AI信用・ドル**：[Reuters 2026-10-28 04:03 UTC](https://www.reuters.com/world/asia-pacific/ai-worries-expose-dollars-hot-money-problem-2026-10-28/)は海外資金の米AI株/債券集中と、AI信用不安時の資金引揚げ→ドル安という条件付きの伝播を分析。一方、ドル調達逼迫時は一時的ドル高もありえる。**新しい研究経路の提起であり信用OAS/CDS→SOX→為替の実証済み因果ではない。判定未判定**。反証：金利差・他市場リスクを統制して標本外先行効果がない。
- **EIA**：[公式予定](https://www.eia.gov/petroleum/supply/weekly/schedule.php)上、10/23週の週報公表は**2026-10-28 10:30 EDT=23:30 JST**。照合19:52 JSTでは**未公表時間帯**。APIの−2.03百万bblをEIA確定値扱いしない。公表後に原油/留出油/輸出を改訂・対象週とともに別記。
- **原油同期裁定・Ras Tanura原油追加輸出減・ロシア軽油米荷揚げと米ULSD・日本船社実現利益・AI信用→SOX因果はいずれも未判定。コーン保管キャリー：データ未取得・未判定**。複数年度個別限月清算値CSVはGitHubのツリーに存在せず、利益/標本外成績を作らない。ライセンス生価格・秘密鍵なし。


## 2026-10-28 23:48 JST 定点レビュー追記：EIA公式在庫、Bahriの実現増益とAframax/LR2の貨物分割

**観測時点**：2026-10-28 23:48 JST（14:48 UTC）。以前の仮説/反証条件と2026-10-28 19:52レビューを保持し、以下の**新たに確認した情報のみ**追加。

1. **米原油在庫：当該週の減少は公式統計で支持、個別輸送仮説は未判定**。[EIA公式要約](https://ir.eia.gov/wpsr/summary.txt)／[JSON](https://ir.eia.gov/wpsr/psw00.json)。公表2026-10-28 10:30 EDT（23:30 JST）、対象2026-10-23終了週：商業原油（SPR除外）**前週比−1.9百万bbl、残高410.6百万bbl**、ガソリン**+3.9百万bbl**、留出油**−1.5百万bbl**、製油処理**16.5百万b/d**、輸入**6.4百万b/d**。APIの先行する**−2.03百万bbl**と数値差**約0.13百万bbl**だが、これは**異なる民間速報と政府確定統計の差**であり「EIAの値の改訂」ではない。**反証・追加検証**：次週の在庫戻り、地域別輸入・需要・精製要因を統制して特定の輸送因果が消えること。EIAの留出油在庫減は**ロシア軽油の米国荷揚げを直接証明しない**。
2. **タンカー高運賃→実現利益：個社事例で部分支持を強化**。サウジBahriが**2026年7–9月Q3の結果を10月28日公表**。[TradeArabia（企業発表を再掲）](https://www.tradearabia.com/News/488751/Bahri-Q3-net-zooms-891_Percent-to-%241.36bn-9M-net-surges-587_Percent)／[Bloomberg転載](https://gcaptain.com/saudi-tanker-giant-posts-10-fold-profit-jump-as-ship-rates-surge/)／[Seatrade](https://www.seatrade-maritime.com/tankers/bahri-profit-leaps-almost-900-in-third-quarter)：売上高**SAR14.83bn（前年同期比+504%）**、純利益**SAR5.09bn（+891%）**、Bahri Oilの実現VLCC運賃上昇および傭船増が主因との会社説明。**世界の特定タンカー船主には実現増益例がある**が、原油生産量・運賃以外の操業変化もある。**反証**：費用・稼働率・契約を同条件にすると運賃要因が利益の説明変数にならないこと。**日本郵船/商船三井/川崎汽船の実現タンカー利益は未判定**。Bahriと契約条件が異なるので一律推計しない。
3. **船型別運賃：二次報道で部分支持、実際の約定とは区別**。[Riviera 2026-10-28付記事](https://www.rivieramm.com/news-content-hub/aframaxlr2-tanker-rates-hit-record-highs-as-vlcc-cargo-cascade-boosts-demand-90399)がBRS Shipbrokers**2026-10-26報告**を引用。前週のBaltic Aframax TCEバスケット**約$385,000/日**、中東湾→日本LR2**約$320,000/日**。新造LR2初航海22隻中13隻が原油を輸送しているとの報告。**10月運賃と7–9月Q3利益は別期間**。TD3C/Clarksea/実成約/TCE/日本船社純利益とは別系列。**反証**：BRS原報告と実約定条件で当該参考水準が裏付かない、費用控除後利益が出ない。
4. **他の既存仮説：判定を維持**。Brent–WTIは**同一2026年12月限・同一UTC秒のICE/NYMEX bid/ask未取得のため未判定**。中東追加供給減、ロシア軽油米国価格低下、AI信用OAS/CDS→SOX・為替の先行因果も**未判定**。サウジ攻撃主張は実際の港湾停止・積出減を意味しない。**トウモロコシ12月限−翌3月限：データ未取得・未判定**（複数作物年度の個別限月清算値履歴なし、費用控除後OOS成績未算出）。
5. **次の測定**：EIA詳細表の原油輸出・PADD1留出油輸入、Bahri 4030の正式IR原本・部門別利益、日本3社船型別実績と運航費、同日時・同限月Brent/WTI気配、Russian dieselの入港/通関、AI信用同年限スプレッド、コーンに必要な契約別履歴と取扱許諾。

詳細：[23:48レビュー](../daily/2026-10-28-review-2348-jst.md)／[Bahri・Aframax/LR2](../topics/2026-10-28-bahri-results-aframax-lr2-cascade.md)／[EIA公式週報](../topics/2026-10-28-eia-oil-inventory-official-release.md)。ライセンス付き生データ・秘密情報は掲載していない。


## 2026-10-29 03:49 JST 定点照合（仮説と過去観測を保持）
[当回レビュー](../daily/2026-10-29-review-0349-jst.md)／[金融政策と原油・AI信用](../topics/2026-10-29-fomc-boc-oil-ai-credit.md)。観測2026-10-29 03:49 JST＝10/28 18:49 UTC。
- **新規公表：FRB** [2026-10-28 14:00 EDT（10/29 03:00 JST）公式声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)。FF金利目標**3.75–4.00%据置（10対2、反対2人は25bp利上げ希望）**。政策据置は**新たなOAS/CDSの悪化や株式への影響の実証ではない**。**AI信用→SOX・為替は未判定**。反証：年限・格付・国債金利調整後の信用悪化が続かず、同発行体の株価先行性が標本外で消える。
- **今回新規一次照合：BoC** [2026-10-28公式声明](https://www.bankofcanada.ca/2026/10/fad-press-release-2026-10-28/)で**25bp利上げ、2.50%**。原油高、製油マージン・運送費、物価転嫁を理由として説明。**2027年CPI約3%は予想**。原油コストの金融政策波及を**部分支持**、特定の中東原油純供給減とその定量影響は**未判定**。反証：燃料・輸送費の二次波及が持続せず、需要等調整後に物価の説明力が消える。
- **10/28 Reuters二次報道** [記事](https://live.euronext.com/en/financial-news/oil-prices-rise-about-2-yemen-fighting-stokes-supply-fears)：イエメン当局者談のアデン空港攻撃、14:42 UTC **Brent$115.69/WTI$102.42は場中報道価格**。サウジ製油所の被害は当局未確認。港湾・原油輸出停止、ICE/NYMEX**同一2026年12月限・同一UTC時刻のbid/ask**を証明しない。**中東安全保障リスクは既存の部分支持維持、原油純供給減・Brent–WTI縮小裁定は未判定**。反証：実積出維持・運賃/保険料の平常化、純裁定が費用控除後成立しない。
- **海運**：Bahriの2026Q3個社実現増益という**以前の部分支持を維持**。日本郵船・商船三井・川崎汽船の増分利益は**未判定**（10月運賃と7–9月決算は異なる）。反証：実際の成約TCEや部門利益が燃料・保険・傭船費用を差引くと増えない。
- **ロシア軽油**：精製回復の以前の部分支持を維持、**11月実荷揚げ・米国ULSD価格効果は未判定**。反証：通関未確認、到着後も需要・在庫・輸出等を統制すると価格効果なし。
- **トウモロコシ12月限−翌3月限：データ未取得・未判定**。複数作物年度の同日・個別限月清算値・保管費・金利・公表時点基差の履歴未登録。予測精度・損益・有意性を推測しない。反証：年度外・費用控除後の20営業日予測効果が再現しない。
- **次**：ICE/NYMEX同期bid/ask、港湾積出量・同航路運賃/保険、船主ネットTCEと日本3社決算、ロシア製品米港通関、AI信用同条件OAS/CDS、CME履歴のライセンス確認。有料原系列・秘密鍵等はGitHubに保存しない。


## 2026-10-29 07:52 JST 定点照合（元の仮説・過去の判定を保持）

[日次レビュー](../daily/2026-10-29-review-0752-jst.md)／[Alphabet・Microsoft一次決算と信用市場](../topics/2026-10-29-alphabet-microsoft-ai-cashflow-credit.md)。照合時点2026-10-29 07:52 JST（10/28 22:52 UTC）。前回03:49 JST後の公表・米市場引けを追加。

- **Alphabet 2026Q3（7–9月実績、10/28米国時間の通常取引引け後公表）**：[SEC公式EX-99.1](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm)。売上高**$127.577bn（+25%）**、Cloud売上**$30.709bn（+103%）**、連結営業利益**$40.576bn（+30%）**。営業CF**$42.290bn**、有形固定資産購入**$51.355bn**で当期FCF**−$9.065bn**（Q2 −$5.855bn）、ただし直近12か月FCFは**+$19.747bn**、9月末現金等流動性**$265.098bn**。Q3の社債ネット調達**$28.7bn**と株式ATMネット調達**$12.4bn**は**7–9月中の資金調達実績**で、10/28以後に同額の新規調達があった意味ではない。GAAP純利益**$26.170bn**の前年比減には営業外の株式投資評価損**−$8.664bn**が関係し、営業利益の増加と矛盾ではない。**判定：AIクラウド実売上の成長と設備投資キャッシュ負担の併存は個社実績で部分支持。信用OAS/CDS悪化・倒産リスクの急変、SOX・為替への先行的因果は未判定。** **反証**：翌四半期以降のFCF回復、同発行体同年限社債CDS/OASと借換え条件の悪化なし、金利・業績を統制した株価先行性が標本外で消えること。
- **Microsoft FY2027 Q1＝暦年2026年7〜9月決算（10/28米国引け後公式公表）**：[Microsoft公式](https://news.microsoft.com/source/2026/10/28/microsoft-announces-first-quarter-results-2/)。売上**$92.3bn（+19%）**、営業利益**$45.9bn（+21%）**、Microsoft Cloud**$63.9bn（+30%）**、Azure売上成長**+48%**。**需要実績は部分支持／MicrosoftのCAPEX・リース/FCFと信用価格への波及は未判定**。反証：顧客のクラウド購買・成長継続性が弱く、収益化が投資支出に追いつかない。
- **10/28米株通常取引引けと原油参考清算値**：[Reuters 10/28市況](https://au.investing.com/news/economy-news/stocks-get-ai-lift-dollar-holds-steady-ahead-of-fed-decision-4719603)。株式通常引けは**10/28 16:00 EDT＝10/29 05:00 JST**、S&P500**+0.28%（7,743.97）**、Nasdaq**+0.27%（26,549.85）**。**引け後決算の反応を引け値へ混入しない**。原油10/28報道参考清算値Brent**$115.32**、WTI**$102.78**は**同2026年12月限・同一UTC秒の両脚約定可能bid/askではない**。Brent–WTI裁定縮小**未判定**。反証：品質・輸送費用調整後の純裁定余地/輸出増/同時刻差の縮小が確認できない。
- **中東純供給減／海運利益／ロシア軽油**：中東安全保障/輸送・高運賃の既存部分支持、**追加純供給減は未判定**。Bahriの**2026Q3個社実現増益は既存部分支持**だが日本3社の10月高運賃に伴う実利益は未判定。ロシア軽油の精製回復の既存部分支持と11月米港着荷予定を維持、**米港実荷揚げ・ULSD価格因果は未判定**。次は同一期の積出・実成約TCE、3社船種別利益、船名/入港/通関・PADD1輸入を照合。
- **トウモロコシ12月限−翌3月限保管キャリー：データ未取得・未判定**。研究用コード・契約台帳・データ取得案はあるが、複数作物年度の同日個別限月清算値CSVがリポジトリにない。費用・在庫・公表ヴィンテージも揃わず、20営業日後効果や収益・有意性は計算しない。反証：年度外・保管キャリー・費用調整後の予測性がない。
- **次回確認**：Alphabet/Microsoftの実際の信用スプレッド同条件系列、米株決算後の翌通常取引、Brent–WTI同限月同期気配、Saudi Aramco純積出、実成約/船主TCE、ロシア軽油米港受入、CBOT個別限月履歴とライセンス。公表日時・期間・異なる限月を混同せず、ライセンス生データ・秘密情報を転載しない。


## 2026-10-29 11:43 JST 定点照合：AIのFCF選別、Samsung確報、原油外交・ICE12月限満期（元仮説・旧結果を維持）

[11:43レビュー](../daily/2026-10-29-review-1143-jst.md)／[AIキャッシュ創出力とSamsung](../topics/2026-10-29-ai-cashflow-selectivity-samsung.md)／[原油外交・Brent限月](../topics/2026-10-29-crude-diplomacy-near-expiry.md)。照合2026-10-29 11:43 JST＝02:43 UTC、比較07:52 JST。

- **AI実需要と投資キャッシュ**：[Microsoft公式FY2027Q1（10/28公表）](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast)の営業CF$58.000bn−固定資産現金支出$39.367bn＝**FCF+$18.633bn**。前回照合の[Alphabet SEC Q3](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm)の**FCF−$9.065bn**と方向が対照的。[Reuters 10/29 02:31 UTC](https://www.reuters.com/business/cash-is-king-investors-draw-new-battle-lines-ai-spending-boom-2026-10-29/)で米10/28**引け後**のMicrosoft株**+3%超**／Alphabet**約−10%**。Alphabet Search成長の市場予想未達も交絡要因。**FCFの差と株価選別の併存を観測、因果は未判定**。反証：決算サプライズ・金利・時価総額を統制後に株価説明力が消える、または信用同条件スプレッドが悪化しない。
- **Samsung 2026Q3一次確報（10/29）**：[Samsung公式](https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2026-results)売上**KRW195.3兆**、営業利益**KRW107.4兆**、DS部門営業利益**KRW106.5兆**、HBM4需要拡大。連結の10/8既報ガイダンスと10/29事業部内訳を区別。[Reuters 10/29 02:28 UTC](https://www.reuters.com/world/china/global-markets-global-markets-2026-10-29/)のSamsung株**場中−4%超**は確定終値ではない。**AI半導体実需の個社部分支持を補強**、信用リスク/SOX因果は**未判定**。反証：実売上・出荷・価格/マージンの持続性がなく、株価の超過反応を統計的に説明できない。
- **原油場中・外交報道**：[Reuters 10/29 00:28 UTC、価格観測01:32 UTC](https://www.reuters.com/business/energy/us-oil-prices-fall-investors-gauge-risks-mideast-supply-2026-10-29/)のBrent**$114.50**／WTI**$101.74**は**場中の異取引所参考値**。米イラン交渉打診との**二次報道**とサウジ側迎撃**主張**はあるが、原油実積出停止/回復を確認できない。ICE公式[Dec26 Brent最終取引日2026-10-30](https://www.ice.com/products/219/brent-crude-futures/expiry)を追加確認。**両脚同2026年12月限・同一UTC秒・執行可能bid/ask不在→Brent–WTI裁定未判定**。反証：同限月・品質/輸送費控除後に正の裁定余地がなく米輸出も増えない。
- **海運・中東純供給減・ロシア軽油**：10/29新しい実成約TCE・日本3社実現部門利益・サウジ純積出量・11月予定の米国軽油着岸/通関/米ULSD効果は**未判定**。Bahri Q3利益は既存の個社部分支持。反証：港湾/輸送費・稼働日数/保険/通関の実績が仮説を支持しない。
- **トウモロコシ12月限−翌3月限：データ未取得・未判定**。公開GitHubの計画・コード・契約台帳を照合。複数作物年度の個別限月清算値、キャリー/基差の事前公表ヴィンテージが無いため統計、20営業日後損益、OOSは推測しない。反証：必要データ取得後の年度外・費用調整済み予測性がない。

**次**：米国10/29通常取引終値と信用CDS/OAS同商品・同年限、Brent Dec26満期前とJan27切替後の同期bid/ask、Yanbu/Ras Tanura輸出・タンカー実現利益、ロシア軽油米港実荷揚げ、CMEの利用許諾済み複数年度清算値。情報提供元の公表・対象期・観測時刻を混同しない。生価格・秘密鍵を転載しない。


## 2026-10-29 15:45 JST 定点照合（仮説・過去の観測は保持）
[15:45レビュー](../daily/2026-10-29-review-1545-jst.md)／[中東・米国の原油輸出推計差](../topics/2026-10-29-saudi-us-export-estimates-physical-premium.md)。照合2026-10-29 15:45 JST＝06:45 UTC、比較11:43 JST。
- **中東原油量とリスクプレミアム**：[Bloomberg原稿のRigzone掲載、2026-10-28 10:55 EDT](https://www.rigzone.com/news/wire/saudi_oil_exports_booming_despite_attacks-28-oct-2026-184954-article/)にサウジ10月途中の輸出数量推計は**Vortexa 6.5百万b/d（9月6.6）、TankerTrackers 6.99、Kpler 5.4（9月比減）**と不一致。Vortexaは紅海2.4→2.5、湾岸4.2→4.0百万b/d。AIS停止など観測差を明示。General IndexによるOman–Dubai現物ディファレンシャルも**9月約$34→10/27約$6/bbl**との報道を参考記録（時系列生データ・査定法は未取得）。**供給減のみが高値主因という強い仮説には反証方向の状況証拠。ただし10/27以降の港湾純供給減・価格寄与率は未判定。中東安全保障・航路制約は既存部分支持維持**。**反証・追試**：同じベンダー・同一品目/港湾・同一週で積出の実減が継続し、戦争保険/ネット運賃と価格差が一致しない／反対に積出と運賃が正常化してリスクプレミアムが消える。
- **Brent–WTI縮小裁定**：[Reuters 10/28 14:39 UTC](https://www.reuters.com/business/energy/us-crude-stocks-distillate-inventories-fall-gasoline-stocks-rise-eia-says-2026-10-28/)でEIA10/23週の原油輸出**4.85百万b/d（前週比+1.4）**、Kpler観測船積みは**約1百万b/d低い**との指摘。EIA原週報要約は[一次](https://ir.eia.gov/wpsr/summary.txt)、輸出詳細表の直接照合は残件。**同月同UTC秒ICE/NYMEX bid/ask未取得、2026 Dec26 Brent 10/30限月満期に注意。判定未判定**。**反証**：輸出増が推計差調整で消える、品質/運賃調整後の正の執行可能裁定がなく同時刻スプレッドの縮小も再現しない。
- **ロシア軽油**：[Reuters 10/29 03:51 UTC価格観測の原油記事](https://www.reuters.com/business/energy/us-oil-prices-fall-investors-gauge-risks-mideast-supply-2026-10-29/)にJ.P. Morganのロシア**製油所原油処理+350千b/d→4.0百万b/d**との**推計**。製品別軽油出荷や米港での荷揚げではない。**精製回復の既存部分支持を補強、対米実輸入/米ULSD価格下落因果は未判定**。**反証**：精製処理の確報と見積が不一致、11月に米港着荷/通関なし、需給調整後にULSD価格下落なし。
- **AI実需要 vs 信用**：[Reuters Samsung 10/29](https://www.reuters.com/world/china/samsung-posts-record-profit-q3-ai-chip-boom-2026-10-29/)によるとHBM2027年分売約済みだが、需給逼迫見通し・株主還元方針（次回2027年1月）で市場期待が分かれた。株価**一時−6.2%は場中**。[Reuters 05:32 UTC](https://www.reuters.com/world/china/global-markets-view-europe-2026-10-29/)のAlphabet約−10%、Microsoft+2.9%は**前日米通常引け後**。**個社実需支持維持、FCFと期待修正による株価選別の部分整合。CDS/OASの同発行体/同年限→SOX・為替の因果は未判定**。**反証**：決算サプライズ・利回り・売買時間等を統制すると信用の先行性が消える。
- **海運**：高運賃・輸送リスクは既存部分支持、Bahri2026Q3個社増益は維持。日本郵船・商船三井・川崎汽船の10月運賃による実利益は**未判定**。**反証**：実成約TCE/契約期間と費用控除後の部門利益が増えない。
- **トウモロコシ12月限−翌3月限**：repo内に複数作物年度の個別限月清算値履歴がなく**データ未取得・未判定**。費用控除後20営業日効果・年度外OOSは計算せず。**反証**：適法に取得したデータと事前公表ビンテージで年度外・費用控除後の予測力が再現しない。

**次**：EIA原油輸出詳細表とAIS船積み・サウジ3社推計の同一対象再照合、ICE Dec26/Jan27とNYMEXの同限月同期bid/ask、船型別船主TCE、日本3社決算、ロシア製品通関、AI同年限OAS/CDS、CME ZC個別契約の履歴ライセンス。生ティック・有料AIS・秘密情報は保存しない。


## 2026-10-29 19:49 JST 定点照合：EIA原油輸出一次統計・韓国半導体の確定終値（元仮説・旧判定を保持）
[19:49レビュー](../daily/2026-10-29-review-1949-jst.md)／[米原油輸出詳細](../topics/2026-10-29-saudi-us-export-estimates-physical-premium.md)／[AI決算と株価選別](../topics/2026-10-29-ai-cashflow-selectivity-samsung.md)。
- **Brent–WTI・原油輸出**：[EIA公式週次表](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=W&n=PET&s=WCREXUS2)（**公開10/28、観測10/29 19:49 JST、対象週10/23終了**）で米原油輸出**4,854千b/d、前週3,442千b/d、差+1,412千b/d**を一次確認。Reuters報道4.85/前週+1.4百万b/dは丸め値と照合できた。ただしKplerとの差約1百万b/d、同12月限同時刻ICE/NYMEX執行可能気配・輸送費・品質差は未解消、**輸出裁定未判定**。**反証**：正の純採算余地がなく、定義を揃えた輸出と価格差の縮小が再現しない。Brent Dec26最終取引10/30、ロール混入禁止。
- **韓国半導体・AI株**：[聯合ニュース10/29 16:34 KST](https://en.yna.co.kr/view/AEN20261029009452320)で**15:30韓国確定終値Samsung−4.13%（232,000KRW）、SK hynix+2.62%（1,530,000KRW）、KOSPI−1.24%（5,937.66）**。場中Samsung一時−6.2%とは別時点。**個社AI実需部分支持・株価選別の観測方向は維持、FCF単独因果/CDS→SOX・為替は未判定**。[Reuters 10/29 08:33 UTC](https://www.reuters.com/business/nasdaq-futures-slide-mixed-big-tech-results-test-ai-trade-2026-10-29/)のAlphabet−10.2%/Microsoft+3.6%は米株**プレマーケット**、確定終値ではない。**反証**：決算期待・株主還元・金利の統制後に差が消える、信用スプレッド先行効果なし。
- **中東原油・輸送**：[Reuters 10/29価格観測09:22 UTC](https://www.reuters.com/business/energy/us-oil-prices-fall-investors-gauge-risks-mideast-supply-2026-10-29/)のBrent114.05・WTI101.27は**場中別市場の報道参考値で裁定スプレッドではない**。外交期待は停戦・港湾正常化の確報ではなく、IRGCのタンカー機雷被害「主張」は船名・UKMTO独立確認なし。**輸送リスク既存部分支持、中東追加純供給減未判定**。**反証**：港湾積出が同一定義で維持/回復、実成約TCE/保険が低下。
- **船主利益・ロシア軽油**：Bahri Q3個社の既存部分支持維持、日本3社の10月実現利益は未判定。ロシア軽油の供給回復の既存部分支持維持、米11月着岸実績・米ULSD価格因果未判定。**反証**：船型別純TCE・部門利益が伸びない／米港荷揚げなし・需給統制後ULSD低下なし。
- **トウモロコシ12月−翌3月限**：GitHubの研究ディレクトリに複数作物年度の個別限月清算値履歴なし、**データ未取得・未判定**。20営業日効果・OOS・費用控除後利益を算出せず。**反証**：許諾取得後の個別限月・事前公表ヴィンテージを使った年度外検証で予測性・利益が消える。
- **次**：同期同限月bid/ask、EIA/Kpler同条件照合、原油積出と実成約、日系3社TCE、ロシア軽油米港の実荷揚げ、同年限CDS/OAS・米通常終値、コーン正規履歴。記事本文・ライセンス付き生データ・秘密鍵は掲載しない。


## 2026-10-29 23:44 JST 定点照合（既存仮説・過去判定は保持）
[当回レビュー](../daily/2026-10-29-review-2344-jst.md)／[AI場中・Microsoft社債](../topics/2026-10-29-ai-cashflow-selectivity-samsung.md)／[中東現物とプレミアム](../topics/2026-10-29-saudi-us-export-estimates-physical-premium.md)／[BEA一次資料](../topics/2026-10-29-fomc-boc-oil-ai-credit.md)。照合2026-10-29 23:44 JST（14:44 UTC）、比較19:49 JST。
- **新規BEA一次統計（公表10/29 08:30 EDT）**：[GDP advance](https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026)は**2026Q3実質GDP+3.4%前期比年率（Q2+2.2%）**、情報処理設備を含む投資が一因。[9月PCE](https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026)は**総合+3.6%前年比／+0.5%前月比、コア+3.1%前年比／+0.3%前月比**。Q3 PCE前期比年率+2.1%と9月前年比3.6%は比較不能。GDPは速報、11/25改訂予定。**マクロ需要の底堅さ・インフレ継続の材料は追加／信用→株価因果未判定**。**反証**：設備投資寄与が改訂で縮小し、金利/成長調整後の信用先行性が消える。
- **新規米株通常場中（Reuters価格観測10/29 09:56 EDT）**：[記事](https://www.reuters.com/business/nasdaq-futures-slide-mixed-big-tech-results-test-ai-trade-2026-10-29/)の**Alphabet−13%、Microsoft−0.5%、SOX−1.8%、Nasdaq−1.64%**。前回19:49の寄付き前気配は異なるセッションで**米10/29確定終値は未取得**。株価選別の観測は継続するが、広告成長・期待・信用等が交絡。**CDS/OAS→SOX/為替は未判定**。**反証**：決算・金利統制で信用先行性消失。
- **新規Microsoft計画起債報道（Bloomberg初報/Benzinga10/29 09:29 ET）**：[記事](https://www.benzinga.com/markets/tech/26/10/62696205/microsoft-goes-jumbo-25-billion-bond-sale-in-the-works)で**少なくとも$25bn・最大10トランシェの米ドルIG債計画**。**予定＝発行済みではない**。AAA企業の調達多様化と信用ストレスは別。**AI外部資金調達の事例を部分支持、信用悪化・市場波及未判定**。**反証**：実発行の見送り・縮小、同年限格付調整後スプレッド悪化なし。次：SEC原本/最終条件、社債新発プレミアム/CDS。
- **原油更新（Reuters10/29価格観測13:14 UTC）**：[記事](https://www.reuters.com/business/energy/us-oil-prices-fall-investors-gauge-risks-mideast-supply-2026-10-29/)で参考場中**Brent $113.77、WTI $100.78**。外交期待が価格下落と併存。[WSJ 10/29記事](https://www.wsj.com/finance/commodities-futures/oil-is-gushing-out-of-the-gulf-why-are-prices-still-above-100-a-barrel-3ccff61d)は湾岸原油積出の回復と高輸送費・将来不安を区別。**リスクプレミアム説明に状況証拠、追加純供給減は未判定**。ICE/NYMEXの**同2026/12限・同UTC秒執行bid/ask未取得につきBrent–WTI裁定/縮小未判定**。10/30Brent Dec26最終取引、ロール混入禁止。**反証**：同一条件の純積出減が高価格を十分説明する、または運賃/リスク調整後に価格差の説明力が消える／純裁定採算なし。
- **海運利益・ロシア軽油**：新たな実成約TCE・日本郵船/商船三井/川崎汽船の10月利益、ロシア軽油11月米港実荷揚げ/ULSD価格効果の確報なし。**BahriQ3の既存部分支持／日本3社未判定、ロシア製油処理回復の既存部分支持／製品輸入・価格因果未判定**。**反証**：船主純TCE/部門益増なし、予定船の通関なし・価格変化に独立な説明力なし。
- **トウモロコシ12月限−翌3月限：データ未取得・未判定**。研究ディレクトリの契約台帳・コード・データ入手計画は存続するが、複数年度の同日個別限月清算値履歴なし。単日差を20営業日先利益や有意性に外挿しない。**反証**：適法取得した同契約データで年度外・キャリー/取引費用控除後の予測性と利益が再現しない。
- **次**：BEA改訂、米10/29通常引け、Microsoft実発行条件・CDS/OAS、ICE/NYMEX同期同限月価格とWTI Midland/MEH・実運賃保険、サウジ積出同ベンダー、船主純利益、日本3社IR、ロシア米港通関、CME許諾済個別限月履歴。記事本文・ライセンス有料原系列・秘密鍵を保存しない。
