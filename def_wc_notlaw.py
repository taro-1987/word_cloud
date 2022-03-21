"""普通のワードクラウド作成"""
import MeCab
from PIL import Image
from wordcloud import WordCloud

def wc_notlaw(analysis_text,
        prefer_horizontal,
        background_color,
        color_map,font_path,
        min_font_size,
        list_add_atop_word):
    mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    results = mecab.parse(analysis_text)

    nouns = []
    for result in results.split('\n')[:-2]:
        x = result.split(',')[0]
        if '名詞' in x:
            nouns.append(result.split(',')[6])
        
    words = ' '.join(nouns)
    wordcloud = WordCloud(width=1280, height=720,
                    prefer_horizontal = prefer_horizontal,
                    background_color = background_color,
                    colormap= color_map,
                    font_path= font_path,
                    min_font_size= min_font_size,
                    collocations = False,
                    stopwords=set(list_add_atop_word))

    wordcloud.generate(words)
    wordcloud.to_file('wc_image.png')