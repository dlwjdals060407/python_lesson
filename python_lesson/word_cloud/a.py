from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np

with open('C:/Users/User/OneDrive/바탕 화면/python_lesson-main/word_cloud/project.txt', 'r', encoding='utf-8') as f:
    text = f.read()

okt = Okt()
nouns = okt.nouns(text) # 명사만 추출

words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함

img = Image.open('C:/Users/User/OneDrive/바탕 화면/python_lesson-main/word_cloud/temp.jpg')
img_array = np.array(img)

wc = WordCloud(font_path='malgun', width=251, height=201, scale=2.0, max_font_size=250, mask=img_array)
gen = wc.generate_from_frequencies(c)

wc.to_file("a.png")

plt.figure()
plt.imshow(gen)
