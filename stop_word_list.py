"""除外キーワードをカテゴリ順に記載していく"""

# ひらがな
list_hiragana = ['ため','もの','こと','たち','それ','とき','ところ','これ','これら',
'それぞれ','すべて','の','よう','しない','しよう','ほか','した','うち','ごと','いずれ','いつ','ら','われ']
# 法令
list_law = ['同法','法','法律','法令','政令','府令','省令','令','規約','規定','定め',
'附則','附','則','抄','柱書','総則','本文','別表','表','措置','但書き','略']
# 法律の構造を示す表現
list_law_structure = ['編','章','節','款','目','条','項','号']
# 法律の施行に関する表現
list_law_operation = ['公布','施行','適用','準用','改正','削除']
# 位置や文章構造などを示す表現
list_place = ['先','次','前','後','中','内','外','間','上','下','左','右','最初','最後','前段','後段',
'同上','前項','次項','前条','同条','次条','当該','該当','従前','以前','以後','以降','前者','後者']
# 期間・数字を表す表現
list_datetime = ['〇','一','二','三','四','五','六','七','八','九','十','百','千','万',
'二十','三十','四十','五十','六十','七十','八十','九十',
'二百','三百','四百','五百','六百','七百','八百','九百',
'年','週','月','日','時','分','箇月','期','期間','現在','経過',
'末日','一日','期日',
'平成','昭和','大正','明治','年度',
'数','端数','額','小数点','金','費','合計','数値','係数','率','級','円','才']
# 一般的に使用頻度の高い語句
list_common = ['場合','際','者','物','等','他','為','事','その他','並び','以下','以上','以外','以内','未満','全て',
'約','的','限り','旨','例','事項','相当','程度','必要','人','関係','問','欄','型','部分','同一','同様','何','所','別','当たり','用','方','同']
# 分かち書きがうまくいっていないもの（テスト時に見つけたもの）
list_miss = ['責','任','行','員','分の','負','地','種','位','つて','つた','たつ',
'なつ','やう','ずる','ずべ','あへ','除','ニア','名宛',
'容','補','権','口','乗','特','申','状','述','原','審','録','書','定','議']
# 文語体カタカナ
list_oldstyle = ['SURU','NAKI','NAL','niha','Razz','RAZ','NYSL','SIAL',
'之','因','対','求','限','且','此','此れ','及','至','有','無','付','効','何等','其',
'得','煮付け','人我','式','属','作','生','上ノ','禁','関','免','失','通','為之','更','示','欠',
'タル','ヨリ','トス','シテ','ケル','アル','トキハ','セザル','ザル','ノミ',
'ぐる','メタル','ハズ','フル語','スベキコト','クル','スニ','ナク','モノ','ムル','レバ','ヲシテ',
'ハザル','シタル','シタルトキハ','ナキ','ケタル','ラズ','シタルモノト','ナル','ナキトキハ','スコトヲ','ベキ','スベシ','スルコトヲ',
'アルトキハ','フコトヲ','フベキ','スル','ラシムルコトヲ','サザル','テハ','ジタル','ケダ','ナルコトヲ','アルト','セズシテ','ムルコトヲ','ザレバ','リテ','コト','スルトキハ','ヒタル',
'トシテ','フコトナシ','ラシメタル','セザルモノト','ナルトキト','ノモノト','スベキ','サザルモノト','スベキコトヲ',
'ナカリシコトヲ','メザリシトキハ','ゲラルルコトナシ','ニハ','タルモノト','セラレタル','メズシテ','スルヲ','レカヲ','スルニ','アリタルトキ','テモ',
'グル','ニテ','ヒテ','メタルモノト','アリタルトキハ','ナルトキハ','エザル','ケタ','シタルコトヲ','リテハ','ラシメタルトキハ','アラザリシ','メズ','クベキ','エテ','ケザルモノニ','','','']
# カタカナ(文語体カタカナが使用されている法律用)
list_katakana = ['ア', 'イ', 'ウ', 'エ', 'オ', 
'カ', 'キ', 'ク', 'ケ', 'コ',
'サ', 'シ', 'ス', 'セ', 'ソ',
'タ', 'チ', 'ツ', 'テ', 'ト',
'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
'マ', 'ミ', 'ム', 'メ', 'モ',
'ヤ', 'ユ', 'ヨ',
'ラ', 'リ', 'ル', 'レ', 'ロ',
'ワ', 'ヰ', 'ヱ', 'ヲ', 'ン',
'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
'バ', 'ビ', 'ブ', 'ベ', 'ボ',
'パ', 'ピ', 'プ', 'ペ', 'ポ',
'ァ', 'ィ', 'ゥ', 'ェ', 'ォ',
'ッ', 'ャ', 'ュ', 'ョ', 'ヴ']

base_stop_words = \
list_hiragana + list_katakana + list_law + list_law_structure + \
list_law_operation + list_place + list_datetime + list_common + \
list_miss + list_oldstyle

# print(len(base_stop_words))
