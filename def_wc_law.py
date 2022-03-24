"""法律特化モードのワードクラウド作成"""
import MeCab
from PIL import Image
from wordcloud import WordCloud

import stop_word_list

def wc_law(analysis_text,
        prefer_horizontal,
        background_color,
        color_map,font_path,
        min_font_size,
        stop_words):
    mecab = MeCab.Tagger()
    results = mecab.parse(analysis_text)

    nouns = []
    for result in results.split('\n')[:-2]:
        x = result.split('\t')[4]
        if '名詞' in x:
            nouns.append(result.split('\t')[0])
        
    words = ' '.join(nouns)
    wordcloud = WordCloud(width=1280, height=720,
                    prefer_horizontal=prefer_horizontal,
                    background_color=background_color,
                    colormap=color_map,
                    font_path=font_path,
                    min_font_size=min_font_size,
                    collocations=False,
                    stopwords=set(stop_words))

    wordcloud.generate(words)
    wordcloud.to_file('wc_image.png')
