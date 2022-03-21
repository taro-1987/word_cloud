from datetime import datetime

import streamlit as st

import stop_word_list
from def_wc_law import wc_law
from def_wc_notlaw import wc_notlaw

# メインカラム
st.title('ワードクラウド作成アプリ')
st.write('法律に特化したワードクラウドを作成することで、その法律がどんな内容なのかをざっくりと理解することができます。')
analysis_text = st.text_area('▼解析したい法律の全条文を入力してください。',
height=400,placeholder='民法くらい長い法律でも分析可能です。')
st.caption('※だいたいの法律の条文は、[このサイト](https://elaws.e-gov.go.jp/)からダウンロードできます。')

analysis_button = st.button('作成')

# サイドバー
st.sidebar.header('-- 各種設定 --')

background_color = st.sidebar.selectbox(
    '●背景色',('white', 'black'))

color_map = st.sidebar.selectbox(
    '●カラーマップ',
    ('rainbow','spring','summer','autumn','winter','bone'))

font_weight = st.sidebar.slider('●文字の太さ（おすすめは5）',
    min_value=1, max_value=9, value=5)
font_path = f'Fonts/ヒラギノ角ゴシック W{font_weight}.ttc'

min_font_size = st.sidebar.slider('●文字の大きさ',
    min_value=5, max_value=50, value=20, step=5)
st.sidebar.caption('※大きくするほど表示される単語が少なくなります。') 

prefer_horizontal = st.sidebar.slider('●縦書きの混ざり具合（おすすめは1）',
    min_value=0.0, max_value=1.0, value=1.0, step=0.1)
st.sidebar.caption('※1に近づくほど、縦書きが減ります（「1」で縦書きなしになります）。') 

add_stop_word = st.sidebar.text_input('●除外したい単語があれば入力してください（複数指定する場合は、全角スペース空けて入力）。')
list_add_atop_word = add_stop_word.split('　')
stop_words = stop_word_list.base_stop_words + list_add_atop_word
st.sidebar.caption('※法律一般に見られる単語はあらかじめ除いています。') 

st.sidebar.write('----------')
select_mode = st.sidebar.checkbox('法律特化モード',value=True)
st.sidebar.caption('チェックを外すと、普通のワードクラウド制作アプリになります。') 

now = datetime.now().strftime('_%Y-%m-%d')

if analysis_text and analysis_button:
    if select_mode:
        wc_law(
            analysis_text,prefer_horizontal,background_color,
            color_map,font_path,min_font_size,stop_words)
    else:
        wc_notlaw(
            analysis_text,prefer_horizontal,background_color,
            color_map,font_path,min_font_size,list_add_atop_word)
    st.image('wc_image.png')
    
    with open('wc_image.png', "rb") as file:
        btn = st.download_button(
        label='画像ダウンロード',
        data=file,
        file_name=f'wc_image{now}.png')
elif analysis_button:
    st.write('条文を入力した後にボタンを押してください！')

st.write('----------')
st.caption('©️ 2022 shotaro') 