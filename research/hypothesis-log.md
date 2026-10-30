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


## 2026-10-30 03:51 JST 定点照合（元仮説・過去の反証条件は保持）

[定点レビュー](../daily/2026-10-30-review-0351-jst.md)／[輸送費・ロシア軽油](../topics/2026-10-30-freight-costs-and-russian-diesel.md)／[ECB・Microsoft](../topics/2026-10-30-ecb-microsoft-funding.md)。照合時点2026-10-30 03:51 JST=2026-10-29 18:51 UTC。米10/29確定終値は**未観測**。

- **輸送費・実現利益を分離**：[Reuters 2026-10-29 16:39 UTC](https://www.reuters.com/business/energy/soaring-freight-rates-add-54-billion-shells-debt-squeeze-totals-margins-2026-10-29/)のShell 2026Q3説明は船舶リース費用評価の前Q比**$5.4bn増＝非現金会計上のリース負債/純負債への影響**（同額の現金運賃支払ではない）。TotalEnergies CEOは輸送費**約$2–3/bbl→$25/bbl**、Q3の液体燃料実現価格が前Q比**$6/bbl低下**した主要因と説明。**輸送費高騰の荷主収益への波及を個社報道で部分支持**。**日本郵船・商船三井・川崎汽船の実現TCE/営業利益増は未判定**。**反証**：同一船型・航路の実成約、費用・契約差調整で費用転嫁が再現せず、実船主の保険等控除後利益が増えない。
- **ロシア軽油**：[Reuters 2026-10-29 15:47 UTC](https://www.reuters.com/business/energy/russia-extend-diesel-export-ban-use-quotas-fulfil-us-deal-sources-say-2026-10-29/)の匿名関係者2人による**11月の例外輸出割当200万トン（10月50万トンの4倍）計画**、年末までの輸出制限延長見込み。政府令は**11月初め予定で未確認**。3隻航行・4隻目出港予定も米港荷揚げの証拠ではない。精製稼働率の月初末+25%は匿名推計で軽油生産実績ではない。**供給回復余地は部分支持、米国実輸入・ULSD価格への因果は未判定**。**反証**：政府令未発出・枠未消化・米港通関なし・米需給/季節を統制後価格効果なし。
- **AI信用／Microsoft**：[Reuters 2026-10-29 18:01 UTC](https://www.reuters.com/business/finance/microsoft-expects-raise-25-billion-us-bond-sale-source-says-2026-10-29/)は**募集自体を規制当局書類で確認**、約**$25bn**・最大10トランシェ（2～40年）は関係者報道の**計画額**。 [初期価格提示の二次引用](https://www.investing.com/news/stock-market-news/microsoft-seeks-at-least-25-billion-in-first-bond-sale-since-2017-4983281)の2年米債+50～55bp、40年+130～135bpは**初期ガイダンス**で最終約定・受渡（11/4予定）・OAS/CDSではない。**外部資金調達の多様化の根拠を追加、信用スプレッド→SOX/為替の因果は未判定**。**反証**：既発債/AAA対照と比較してプレミアム小、信用・株/為替に同期/先行関係なし。
- **ECB**：[公式金融政策決定2026-10-29](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp261029~9a493adf17.en.html)は預金2.50%・主要2.65%・限界2.90%で据置、エネルギーショックによるインフレ上振れ/成長下振れと金融環境引締まりを明記。**中銀のコストインフレ警戒は支持**するが自動的な利上げや実際の生産減を証明しない。**反証**：二次的な基調物価・賃金影響が見られず、信用環境も緩和に戻る。
- **原油・Brent–WTI**：[Reuters 2026-10-29 13:35 EDT（10/30 02:35 JST）](https://www.reuters.com/business/energy/us-oil-prices-fall-investors-gauge-risks-mideast-supply-2026-10-29/)のBrent $114.92/WTI $102.12は**報道場中参考値**。同12月限・同UTC秒の執行可能bid/askなし、ICE Brent Dec26の10/30満期にも注意。**輸出裁定は未判定**。**反証**：品質/輸送/金融コスト控除後の同期純裁定・輸出増・スプレッド縮小が同時成立しない。安全保障上の攻撃主張は積出純減の確報ではない。
- **トウモロコシ保管キャリー**：`research/corn-dec-mar/data/input/futures_daily.csv`はGitHub 404。履歴の個別限月清算値・保管/金利/基差の時点整合データなし。**データ未取得・未判定**を厳守し20営業日後リターン、統計的有意性、取引可能利益を推測しない。**反証**：取得後の年度外・費用控除・当時公表情報のみの検定で再現性がない。


## 2026-10-30 07:46 JST 定点照合（元仮説・反証条件と旧判定は保持）
[当回レビュー](../daily/2026-10-30-review-0746-jst.md)／[日本郵船の通期修正予想](../topics/2026-10-30-nyk-outlook-business-mix.md)／[AI米通常引けとMicrosoft社債注文](../topics/2026-10-30-ai-us-close-bond-demand.md)。照合2026-10-30 07:46 JST＝2026-10-29 22:46 UTC、前回03:51 JSTと比較。
- **海運・日本郵船（今回初照合、開示日10/29）**：[NYK10/29正式開示](https://www.nyk.com/ir/news/2026/__icsFiles/afieldfile/2026/10/29/20261029jpn.pdf)で2027/3期**通期予想**の営業利益**1,850億→2,100億円（+13.5%）**、経常利益**2,500億→3,350億円（+34.0%）**、純利益**2,400億→3,300億円（+37.5%）**（比較は8/5予想、決算実績ではない）。理由は**コンテナ運賃上振れ→ONE持分法利益予想改善、ドライバルク/エネルギー堅調**。**海運市況が業績予想に波及する部分支持材料**だが、**中東スポット原油タンカー高運賃→NYKの実現部門利益増**の直接証拠ではなく**未判定**。**反証**：11/5上期確報・事業別利益でエネルギー部門の利益/純TCEが増えない、予想増がONE・コンテナや為替のみで説明される。Bahri既存部分支持は維持。
- **AI米10/29確定引け**：[Reuters](https://www.reuters.com/business/nasdaq-futures-slide-mixed-big-tech-results-test-ai-trade-2026-10-29/)と[AP](https://apnews.com/article/wall-street-stocks-dow-nasdaq-2c26b0b1bbc3bfab9f3f4b902172f458)でS&P500**7,720.39（−0.30%）**、Nasdaq**26,184.72（約−1.38%）**、SOX**約−1.4%**、Alphabet**約−12.6%**。前回03:51の米通常**場中値を確定終値に置換**。広告売上鈍化・決算サプライズ・金利等の交絡があり、**資金負担と株価選別の個社部分支持**、**信用CDS/OAS→SOX・為替の因果は未判定**。**反証**：経済・決算情報統制後に信用指標の先行性なし。
- **Microsoft社債需要（Reuters10/29 15:49 ET＝10/30 04:49 JST更新）**：[UPDATE5](https://www.schwab.wallst.com/schwab/Prospect/research/stocks/news.asp?doc=3200-nL3N46F1LB-9&symbol=MSFT)の関係者情報では**想定$25bn前後に$100bn超の注文**（4倍超）。**注文簿≠確定発行額・最終条件・受渡・発行後OAS**。信用力の高いMicrosoftの資本市場アクセスを示す**個社の支持材料**であり「AI業界全体の信用市場閉鎖」には反証方向だが、脆弱なAI企業へ外挿禁止。**反証**：最終スプレッドが同年限AAA既発債対比著しく高い、注文減少、二次CDS/OASの悪化。
- **原油10/29清算**：[Reutersの10/29取引日終値更新](https://www.reuters.com/business/energy/us-oil-prices-fall-investors-gauge-risks-mideast-supply-2026-10-29/)はBrent**$114.88/bbl（−0.38%）**／WTI**$102.00/bbl（−0.76%）**。**異取引所の清算時刻・限月・算定規則の違いで単純差$12.88を執行可能同期スプレッドとみなさない**。ICE Brent Dec26は10/30最終取引。同限月同UTC秒bid/ask、港湾費・品質・運賃・保険未取得につき**Brent–WTI縮小裁定は未判定**。**反証**：純採算余地なし、輸出量定義統一後に拡大→縮小の関係なし。
- **ホルムズLNGの長期ヘッジ（油と区別）**：[Reuters 10/29](https://www.reuters.com/business/energy/qatarenergy-buys-us-other-lng-hedge-future-hormuz-disruptions-2026-10-29/)によるQatarEnergyの米LNG年最大7百万トンの長期購入契約（受渡2030/31年頃以降）は、企業がホルムズリスクへの対策を実行している材料。**2026年原油の追加純供給減、実物VLCC運賃、船社利益の証拠ではない**。中東輸送不安の既存部分支持、純積出減は未判定。
- **ロシア軽油**：新しい政府政令・11月米港実荷揚げ/米ULSD価格効果は確認できず**未判定**。10/29の輸出枠拡大計画はあくまで未確定。**反証**：政府令不成立、米港通関なし、需要調整後価格効果なし。
- **トウモロコシ12月−翌3月限：データ未取得・未判定**。研究計画/ソース台帳を再点検したが、複数作物年度の個別清算値履歴CSVは未取得。20営業日後リターン/収益性/統計的有意性/OOSを推測しない。**反証**：取得後の同年限同日清算・当時ヴィンテージ/保管費・金利で年度外費用控除後の予測性が再現しない。

**次**：NYK11/5半期IR・3社の船種別純TCE、Microsoft最終債券条件とネオクラウド信用比較、ICE/NYMEX同月同UTC秒売買気配、サウジAIS/港純積出、ロシア軽油米国通関、CME個別限月の適法な時系列入手。ニュース本文・ライセンス付き生相場・秘密鍵は公開しない。


## 2026-10-30 11:48 JST：AIクロスアセットの場中リスクオフとホルムズ新主張（元仮説を保持）

[今回の定点レビュー](../daily/2026-10-30-review-1148-jst.md)／[AI信用と株・債券・円](../topics/2026-10-30-ai-cross-asset-riskoff-credit-gap.md)／[ホルムズ未検証主張とBrent満期](../topics/2026-10-30-hormuz-mine-claims-brent-expiry.md)。**観測2026-10-30 11:48 JST（02:48 UTC）、比較07:46 JST**。

- **AI投資採算懸念とクロスアセットの同時変動**：[Reuters 10/30 02:45 UTC](https://www.reuters.com/legal/transactional/global-markets-global-markets-2026-10-30/)の**場中**ではKOSPI約−5%、日経約−3%、Nasdaq100先物約−1.4%、米10年金利約4.91%（東京時間に7bp超低下）、米2年約4.57%（8bp超低下）、ドル円157.47円（円約0.2%高）。**これらは同秒抽出値でも確定終値でもなく、報道の市場解説を信用市場先行の実証と扱わない**。米10/29 Alphabet通常引け約−12.6%は**前回既記録**、Intel約−23%・Amazon約−7%は**引け後参考値**。**判定：一般的なAI投資採算懸念と株安・国債高・円高の併存は観測／CDS・OAS→SOX・為替の因果は未判定**。**反証**：同発行体・年限のCDS/OASが拡大していない、先行効果が決算/米金利/他リスク統制後に消える、日中の値動きが終値で消える。
- **中東航行と実供給**：[Reuters 10/30 02:27 UTC、価格参照01:22 UTC](https://www.reuters.com/business/energy/oil-rises-supply-concerns-houthis-attack-saudi-arabia-2026-10-30/)による**場中**Brent $115.74、WTI $102.72/bbl（それぞれ+0.75%、+0.71%）。フーシ派のRas Tanura/Rabigh/Abqaiq攻撃は**主張**、サウジ側の巡航ミサイル迎撃は**当局発表**、革命防衛隊のタンカー3隻機雷炎上も**主張**であり、**船名/IMO・UKMTO独立確認・施設損壊・実積出純減は未確認**。**判定：安全保障・輸送懸念の既存部分支持を維持、追加純供給減・タンカー個社利益は未判定**。**反証**：独立航行事故/港湾停止を裏付けず、同ベンダー同港湾の積出正常化、運賃/保険料の鎮静化。
- **Brent–WTI縮小輸出裁定**：ICE公式で**Brent 2026/12月限の最終取引日は10/30**。上記参考価格は**同限月・同UTC秒の両脚執行可能bid/askではない**。WTI期近との混用と限月ロールの見かけの変化を禁止。実地Midland/MEH・品質・保険・港費・船賃未調整で**未判定**。**反証**：同月同秒・費用調整済み純裁定が成立せず、実米輸出フローも追随しない。
- **その他**：日本郵船の10/29業績上方修正は**予想（コンテナ/ONE等を含む）**、Bahri 2026Q3実現増益は既往の個社部分支持。日本郵船・商船三井・川崎汽船の**10月タンカー起因実現増益は未判定**。ロシア11月軽油**200万トンは関係者の輸出枠計画**（Reuters 10/29 15:47 UTC）、政府正式命令・米港荷揚げ・ULSD価格因果は未判定。
- **トウモロコシ12月限−翌3月限：データ未取得・未判定**。複数年度の同日個別限月清算値履歴CSVが研究ディレクトリに存在せず、単日価格を保管キャリーの利益や20営業日後予測の検定値に代用しない。**反証**：費用・公表時点キャリー調整後の年度外予測/運用成績が再現しない。

**次**：日銀10/30正式決定とアジア確定引け、AI信用同ベンダー同年限OAS/CDS・先行性、ICE Dec26最終/Jan27ロール、UKMTO船名/IMOと港湾実積出、実成約TCE、日本船社事業別利益、ロシア政令/11月入港、CBOTライセンス済み個別限月履歴。ライセンス生テープ、AIS、報道全文、秘密鍵は転載しない。

## 2026-10-30 15:45 JST 定点照合：日銀正式決定・UKMTO事故更新（過去仮説を維持）

[15:45定点レビュー](../daily/2026-10-30-review-1545-jst.md)、[日銀金融政策・AI競合仮説](../topics/2026-10-30-boj-policy-etf-ai-inflation.md)、[UKMTOの事故訂正追補](../topics/2026-10-30-hormuz-mine-claims-brent-expiry.md)。**照合2026-10-30 15:45 JST（06:45 UTC）**。

- **日銀（新規一次情報、10/30 12:02 JST公表）**：[政策声明](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k261030a.pdf)で政策金利1.25%据置（8対1）、ETF売却を**2027年1月から簿価年3,300億→8,600億円**（[別紙](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k261030c.pdf)、時価換算約2兆4,600億円、売買代金比約0.1%）と決定。[見通し](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k261030b.pdf)のFY2027コアCPI2.6%（7月比+0.2pp）を確認。**物価予測と実績、将来ETF売却ペースと当日実売却を区別**。原油・中東リスクによる物価圧力は政策当局の見通しと整合、独立寄与率は未判定。**反証**：後続の実物価が下振れ、原油/運賃が落ち着く。**AI信用→株価・為替の因果未判定**。日銀公表という交絡イベントを統制。
- **ホルムズ航行リスク**：[UKMTO公式#185～187](https://www.ukmto.org/)、[Seatrade 10/30](https://www.seatrade-maritime.com/security/tanker-catches-fire-in-hormuz-after-explosives-attached-to-hull)。#187の事故時刻**10/29 22:12 UTC**、爆発物2個→機関室火災・一時航行不能、後に火災消火/次港へ航行再開との更新。#185の炎上船は**ダウ船**と訂正、#186は別件。**IRGC「3隻機雷被害」への独立確証と混同しない**。安全保障の定性部分支持補強、純輸出減・船舶損害全容未判定。**反証**：UKMTO訂正・同ベンダー積出維持・保険/運賃平常化。
- **Brent–WTI縮小裁定**：[Reuters 10/30 03:23 UTC参考値](https://www.reuters.com/business/energy/oil-rises-supply-concerns-houthis-attack-saudi-arabia-2026-10-30/)の**Brent Dec26 116.08/Jan27 112.19ドル**とWTI103.37ドル（限月・気配不明）を区別。**同一限月・同UTC秒のICE/NYMEX執行可能bid/askと品質・輸送/保険費用は未取得→未判定**。反証：純採算余地がなく、価格差縮小とEIA輸出増の時間整合が成立しない。
- **タンカー運賃と海運利益**：Bahri Q3既往部分支持、NYKの10/29予想増額はONE/コンテナ等も含み**日本3社タンカー実現利益未判定**。実成約/TCEは未取得。反証：費用調整後船主TCE・部門益が改善しない。
- **ロシア軽油→米ULSD**：11月200万トンは政府令未確認の予定枠であり**米港荷揚げ・価格因果は未判定**。反証：命令/輸出/米港通関が実現せず需給調整後価格効果なし。
- **トウモロコシDec26–Mar27保管キャリー**：研究計画とスクリプトを確認し、`research/corn-dec-mar/data/input/futures_daily.csv`はGitHub APIで404。許諾済み複数年度個別限月履歴・時点整合的基差/保管費なし。**データ未取得・未判定**。反証：年度外・費用控除後の20日予測力が再現しない。研究結果を推測しない。

**次**：UKMTO再訂正・港湾積出、2027年1月限同UTC秒Brent–WTI双方向気配、東京10/30確定終値と12:02日銀イベント、AI同年限CDS/OAS、海運3社IR、ロシア政令と実荷揚げ、CME個別契約の許諾済み時系列。原仮説・履歴は維持、有料原系列や秘密鍵は保存しない。


## 2026-10-30 19:47 JST 定点照合：東京株確定値、対米ロシア軽油推計、原油予測改訂（元仮説・旧判定保持）

[レビュー](../daily/2026-10-30-review-1947-jst.md)／[AI日本株](../topics/2026-10-30-japan-ai-close-credit-causality.md)／[ロシア軽油](../topics/2026-10-30-russian-diesel-seven-vessels-us-arrivals.md)／[原油予測・限月](../topics/2026-10-30-oil-forecast-survey-brent-roll.md)。**照合2026-10-30 19:47 JST＝10:47 UTC**。初出時刻、本文更新時刻、市場の取引時刻を分ける。

- **AI採算懸念と日本市場**：[株探/フィスコ 10/30 15:34 JST](https://s.kabutan.jp/news/n202610301052/)で東証10/30**確定終値**は日経平均**63,290.11（−1,369.36／−2.12%）**、TOPIX**3,965.07（−38.21／−0.95%）**。[Reuters 10/30記事（本文で引け値へ更新）](https://www.reuters.com/world/asia-pacific/japans-nikkei-slumps-3-tech-stocks-tumble-ai-worries-2026-10-30/)は半導体関連の売り・AI設備投資採算懸念を指摘。前回の**場中**観測から**確定終値**へ更新しただけで、**CDS/OAS→SOX/日経・ドル円の先行因果は未判定**。日銀**12:02 JST**声明・ETF売却**2027/01開始計画**と決算発表は競合イベント。**反証**：同年限・同発行体の信用スプレッド悪化が株価に先行せず、決算サプライズ/金利/日銀ショックを統制した予測力がない。**次**：同UTC時刻のOAS/CDS、日銀発表前後の株/金利/為替、Microsoftの最終社債価格スプレッド。
- **ロシア産軽油の対米航行は推計の部分支持を補強、米価格効果は未判定**：[The Guardian 2026-10-29 20:01 CET初出（10/30 04:01 JST）](https://www.theguardian.com/us-news/2026/oct/29/seven-oil-tankers-288000-tonnes-russian-diesel-sail-us-putin-trump)が[Greenpeace船舶追跡](https://maps.greenpeace.org/maps/gpuk/us-diesel-tanker-tracker/)に基づく**7隻・推計288,000トンの米国方面航行**を報道。以前の「3隻航行」と**重複し得る母集団、合計10隻としない**。米港到着・荷揚げ・通関・国内小売ULSD下落の実績とは別。Reutersの**11月輸出枠200万トン（政府令未確認）**とも別。**反証**：AIS/IMO・積荷/目的港の誤認や米港での受入不成立、輸入が確認されても原油・在庫・需要調整後にULSD価格低下が観測されない。**次**：個別船のIMO・ETA・米税関/港湾確認・EIA PADD1留出油輸入と米国ULSD現物・小売。
- **Brent–WTI縮小裁定は未判定を維持**：[Reuters 10/30 08:45 UTC＝17:45 JST参考場中値](https://www.reuters.com/business/energy/oil-rises-supply-concerns-houthis-attack-saudi-arabia-2026-10-30/)でICE **Dec26 $117.15（10/30最終取引日）、Jan27 $112.99**、NYMEX **WTI $103.79（本文で限月未確認）**。**異限月差、同時刻の執行可能bid/askでない差を裁定利益にしない**。**反証**：Jan27同UTC秒bid/askと現物品質・港費・海運・保険・資金費用を照合すると純裁定が非正、またはその後の輸出・スプレッド縮小に関係しない。**次**：ICE/CME同Jan27同期気配と実積出・実成約運賃。
- **中東のリスク認知は支持方向、実供給純減は未判定**：[Reuters 10/30 09:34 UTC公表・32人調査](https://www.reuters.com/business/energy/brent-2026-view-tops-90-first-time-since-may-mideast-stability-remains-elusive-2026-10-30/)の**2026年平均価格予測**Brent **$92.88（前月$89.05）**、WTI **$86.60（前月$83.90）**、**2026Q4需給赤字約2.7百万b/d／2027年余剰約0.29百万b/d**は**予測/市場認識**。当日先物・EIA実測・サウジ実輸出ではない。**反証**：同母集団実積出が維持・回復し、現物プレミアム・戦争保険・運賃の持続上昇が消えること。**次**：実港湾フロー、保険・fixture、次回予測ヴィンテージと確報の比較。UKMTO事故の以前の部分支持を維持し、3隻機雷被害を独立確認済みとは扱わない。
- **海運利益**：Bahriの既往2026Q3実現増益は**部分支持維持**。日本郵船の10/29通期**予想上方修正**と海運3社の10月高運賃によるタンカー**実利益**は分離。新たな同航路fixture/TCE、3社実現利益がなく**未判定**。**反証**：増収が契約長期固定/コスト増/稼働低下で実現船主利益に結びつかない。**次**：日本3社の部門別決算、費用控除後TCE、契約構成（日本郵船11/5予定）。
- **トウモロコシ12月限−翌3月限保管キャリー：データ未取得・未判定**。`research/corn-dec-mar/`の計画・個別限月の契約台帳・CSVテンプレート・コードは存在。GitHub Contents APIで`research/corn-dec-mar/data/input/`は**404**、複数作物年度の日次個別限月**実測**清算値・保管費・公表ヴィンテージなし。**収益、勝率、p値を計算・推測しない**。**反証**：適法な履歴と当時利用可能な需給/保管費・金利を用い、費用控除後・年度外検証で20営業日後スプレッド予測/損益優位が消えること。**次**：CBOT/CME個別限月の利用許諾、実測履歴、USDA WASDE/NASS公表時点。

**全テーマ**：旧仮説・判定履歴は改変なし。報道全文・ライセンス付価格/AIS原データ・APIキー・秘密鍵はGitHubに追加しない。


- [2026-10-30 23:47 JST：Amazon/Intel決算の一次開示と米株10/30場中急落、Louise 1の攻撃方法、Brent限月ロールを照合](../daily/2026-10-30-review-2347-jst.md)（**Amazon AWS四半期売上+39%／TTM FCF−$42.4bn**により需要と資金負担の併存は個社部分支持を補強。Intel DCAI+78%とPC部門−5%はセグメント別。Reutersの**10/30 09:53 EDT＝22:53 JST場中**Nasdaq−2.21%・SOX−5.7%は確定終値ではない。**同一発行体・年限・時点のCDS/OAS→株価・為替の因果は未判定**）。**Louise 1は10/29発生の既知事故の船名・吸着機雷2個の続報**であり、別件の複数船被害主張と合算しない。**Brent Dec26 $117.14、Jan27 $113.10、WTI $103.94は10/30 12:36 UTCのReuters参考値、WTI限月未明示**のため同限月・同時刻の実行可能裁定は**未判定**。**日本3社のタンカー由来実現増益、中東追加純供給減、ロシア軽油米港荷揚げ・ULSD値下げ**も未判定。**CBOTトウモロコシ12月−翌3月：データ未取得・未判定**。
- [AI一次決算・信用因果の検証ノート](../topics/2026-10-30-amazon-intel-cashflow-us-intraday.md)／[ホルムズLouise 1とBrentロールの検証ノート](../topics/2026-10-30-louise1-brent-roll-followup.md)。**反証条件**：同年限信用プレミアム縮小/横ばいで株が下落なら信用起点説を弱める；輸送費控除後に正のJan27輸出裁定余地なし/輸出が増えなければスプレッド縮小説を弱める；事故後も広域積出回復・保険料/TCE低下なら供給逼迫説を弱める；米軽油実荷揚げなし/統制後値下がりなしなら露軽油による値下げ説を弱める。原仮説・過去判定は保持。


## 2026-10-31 03:51 JST 定点照合：Intel CDS定量悪化、Microsoft社債価格決定、Brent参考値上昇（原仮説・履歴を維持）

[今回のレビュー](../daily/2026-10-31-review-0351-jst.md)／[Intel/AI信用追補](../topics/2026-10-30-amazon-intel-cashflow-us-intraday.md)／[Microsoft発行条件追補](../topics/2026-10-30-ecb-microsoft-funding.md)／[Brent限月・リビア追補](../topics/2026-10-30-louise1-brent-roll-followup.md)。**今回照合2026-10-31 03:51 JST（10/30 18:51 UTC）、比較前回10/30 23:47 JST。米10/30株式市場はまだ通常取引場中**。

- **AI信用市場（新しい定量証拠）**：[Reuters 10/30 Intel記事](https://www.reuters.com/business/intel-warning-sparks-chip-rout-pc-weakness-clouds-turnaround-2026-10-30/)掲載のMarkit**Intel 5年CDS 124.75bp／前日比+17.5bp／過去最高水準**で、**個社信用ストレス増大は部分支持**。同日Intel株約30%安も場中。Reuters [10/30米株記事](https://www.reuters.com/business/nasdaq-futures-tumble-amazon-intel-results-deepen-ai-spending-woes-2026-10-30/)の**Nasdaq総合25,303.37（−3.37%）、SOX約−8.7%はウェブ照合時の場中値**で確定終値ではない。Markit気配の同UTC固定時刻、SOX・他社CDS/OASとの先行比較は未取得。**「Intel信用不安」は支持、「AI全体の信用スプレッドが先導してSOX・為替に波及」は未判定**。Intel PC需要・メモリー・製造支出も交絡。**反証**：Intel以外の同年限AI信用が安定し、時系列上の先行説明力が消える。**次**：10/30米引け、個社CDS時刻/比較、他の同格付けOAS。
- **Microsoft（既往の報道上の募集計画から確定一次情報へ）**：[Microsoft公式2026/10/29価格決定発表](https://news.microsoft.com/source/2026/10/29/microsoft-announces-debt-offerings-7/)によって**$25bn・10系列（変動$2bn／固定$23bn）**、固定クーポン**4.85%～6.35%**、**11/4受渡予定**を確認。高信用力発行体の資金調達アクセスは支持方向で、「AI企業すべてが信用逼迫」に反証。ただし**固定クーポン≠同年限信用OAS**、現時点で約定後の入金とCDS全体の改善は未判定。**反証**：受渡未実施、最終条件改訂、同格付け債に対する異常プレミアム。**次**：SEC最終価格補足と同年限米国債・IG既発債比較。
- **Brent–WTI裁定**：[Reuters原油記事の10/30 **17:07 UTC**市場参考値](https://www.reuters.com/business/energy/oil-rises-supply-concerns-houthis-attack-saudi-arabia-2026-10-30/)、Brent **Dec26 117.75/Jan27 114.03ドル**、WTI **104.79ドル（限月明記なし）**。Dec満期日の期近ロールによる誤読に注意。**Jan27同限月・同UTC秒bid/askと港費/輸送/保険/品質差が未取得のため輸出裁定・スプレッド縮小は未判定**。**反証**：費用控除後裁定余地なし、米輸出増・価格差縮小が確認できない。**次**：同期双方向気配と米湾岸輸出フロー。
- **中東航行・実物と海運**：Louise 1の吸着機雷事故は既往で**安全保障リスク部分支持維持**、IRGC複数被害主張に合算しない。Reuters同日記事が伝えたリビアHamadaパイプラインの**約15,000b/d流量停止（国営石油会社説明）**は別地域・別原因。**湾岸純輸出減、日本3社のタンカー起因実現増益は未判定**。Bahriの既往Q3実益とNYKの10/29利益**予想**は区別。**反証**：湾岸積出回復・船主実現TCEが燃油/戦争保険控除後で低下。**次**：当局港湾実績、航路別fixture/TCE・保険、日本3社事業別確定決算。
- **ロシア軽油**：前回の7隻・推計28.8万トンと輸出枠案以降、独立確認できた正式政令、米港荷揚げ・米ULSD価格への因果証拠は**新たになし・未判定**。**反証**：米入港/通関がない、在庫・原油・需要統制後も価格低下なし。**次**：IMO/港湾・米EIA/PADD、11月政府令。
- **CBOTコーンDec–翌Mar保管キャリー：データ未取得・未判定**。GitHubの`research/corn-dec-mar/data/input/futures_daily.csv`は今回もContents APIで**404**。複数作物年度の個別限月実測清算値、保管費・金利・基差の公表時点資料がなく**取引成績、勝率、p値は未推定**。**反証**：適法データで費用控除後・作物年度外の予測性が再現しない。**次**：データ使用許諾と当時ヴィンテージを揃える。

**保全**：本文追記のみ。既存の仮説と旧判定は削除・書換えせず、有料相場原系列・AIS生データ・記事全文・秘密鍵は保存しない。


## 2026-10-31 07:52 JST 定点照合：Meta信用見通しと10/30米株・原油引け（原仮説・過去判定は保持）

[今回レビュー](../daily/2026-10-31-review-0752-jst.md)／[Meta信用ノート](../topics/2026-10-31-meta-rating-outlook-ai-credit-close.md)／[原油・運賃・軽油ノート](../topics/2026-10-31-oil-russian-freight-and-diesel-update.md)。照合：2026-10-31 07:52 JST＝10/30 22:52 UTC。前回03:51 JSTの観測後に公表・確定した情報を区別する。

- **AI信用（部分支持補強）**：[Reuters 10/30 21:14 UTC](https://www.reuters.com/business/sp-global-revises-outlook-meta-negative-cashflow-concerns-2026-10-30/)：S&PがMeta AA-格付け**見通しのみ**安定的→ネガティブに変更。格付け引下げではない。Meta Q3 FCF -$2.12bnは実績、2026/27のFOCF -$39bn/-$71bnはS&Pの**予測**であり定義も異なる。前回のIntel Markit 5年CDS 124.75bp（+17.5bp）に加え、AI投資負担が個別信用評価へ影響する仮説の**部分支持を補強**。ただし見通し報道21:14 UTCは10/30通常株引け20:00 UTCの**後**であり株安の発表因果には使わない。[Reuters米株引け版](https://www.reuters.com/business/nasdaq-futures-tumble-amazon-intel-results-deepen-ai-spending-woes-2026-10-30/)はNasdaq **25,437.00/-2.86%**、S&P500 **7,580.07/-1.82%**、SOX **-7.2%**、Intel **-28.6%**。前回03:51の場中-3.37%/-8.7%は別観測。**同年限CDS/OASがSOX・為替に先行する因果は未判定**。Microsoft公式10/29 $25bn社債発行条件確定は信用全面閉鎖への反証方向、受渡は11/4予定。**反証**：信用異常プレミアムの同条件広域拡大・先行性がなく、FCF回復/格付け見通し改善。**次**：S&P原文、格付け/信用OAS/株価の時刻整合と翌営業日。
- **Brent–WTI（裁定未判定）**：[Reuters 10/30引け](https://www.reuters.com/business/energy/oil-rises-supply-concerns-houthis-attack-saudi-arabia-2026-10-30/)にICE Brent **Dec26 $117.64**（10/30最終取引日）、別契約**Jan27 $113.43**、WTI **$104.12**（同記事で契約月不明）。10月原油騰落率Brent+13.6%／WTI+15.2%は月末記事の数値で、前回17:07 UTC場中とは異なる。**同2027年1月限・同UTC秒執行可能bid/askとMidland/MEH品質・港費・保険・船賃が未確認のため裁定・縮小未判定**。**反証**：費用調整後に純裁定余地なく輸出も追随しない。**次**：ICE/CME同期気配とEIA輸出。
- **中東供給・運賃（航行リスク部分支持維持、サウジ輸出一律減の強仮説には反証方向）**：同Reutersで**船舶追跡3社中2社が10月サウジ原油輸出は9月より増えたと推定**。UKMTO既往の爆発物・火災事故と広域の輸出純減は別。Reuters [10/30 16:03 UTC、関係者推計](https://www.reuters.com/business/energy/freight-rates-russian-oil-stay-record-highs-amid-tanker-shortage-black-sea-risks-2026-10-30/)でロシアUrals**原油**西部港→インド運送費約**$30/bbl以上**（9月約$20）、Aframax片道**$23m**（9月$13-16m）、Suezmax片道**$30m**（9月$19m）。運送負担増の部分支持だが**軽油航行・船主実約定TCEや日本3社のタンカー起因確定利益とは別**。**反証**：同定義サウジ輸出が実際には継続減、または同航路船主TCE/日本船社純利益が運賃増を反映しない。**次**：港別同期間実積出・保険・実成約、川崎11/4・NYK11/5・商船三井11/9の予定決算。
- **ロシア軽油（政策意向は部分支持、米荷揚げとULSD価格は未判定）**：[Reuters 10/30 13:00 UTC](https://www.reuters.com/business/energy/russia-plans-export-215-million-tons-diesel-november-media-say-2026-10-30/)はノバク副首相のロシアメディア経由**11月輸出215万トン計画／輸出規制2027年1月末延長準備**を報道。10/29匿名関係者の**11月例外枠200万トン案／2026年末延長案**と対象・出所が異なる可能性、政府正式令未確認。7隻/28.8万tは航行推定であり、米港到着・通関ではない。**反証**：政令/割当/着岸不成立、原油/需要/在庫調整後の米ULSD下落なし。**次**：正式令、米税関・港湾、EIA PADD。
- **CBOTトウモロコシDec–翌Mar保管キャリー：データ未取得・未判定**。研究README・台帳・スクリプト・テストを再点検。複数作物年度の個別限月清算値CSV **research/corn-dec-mar/data/input/futures_daily.csv は今回もGitHub API 404**。当時公表ヴィンテージ、保管費・基差/金利・使用許諾も不足。**収益率・勝率・p値は推計しない**。**反証**：費用控除・年度外20日予測性がない。**次**：適法な個別限月日次履歴と当時データを取得。

公表時刻、対象取引日、実績/予測、契約月を混同しない。原仮説と過去の記録は追記のみ。ライセンス付き価格・AIS生データ、記事本文、秘密鍵は転載しない。
