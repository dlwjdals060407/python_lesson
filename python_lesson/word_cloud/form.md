---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
marp: true
---

# ai기사에 대한 워드클라우드 분석

#### **파이썬 워드클라우드 활용을 통한 독서 프로젝트**

</br>

##### 이정민|하길고등학교|2학년

---

# ✨ Project Information

### | **준비 기간**

  </br>

###### 2주

</br>

### | **관련 교과**

  </br>

###### `독서`

---

# 📝 프로젝트 내용

### | 탐구 동기

독서 주제 통합적 글쓰기 부분의 수행평가에서 ai의 주제를 선택한 나는 좀 더 ai에 관련된 기사들을 모아서 ai에 관련된 다양한 정보와 주장을 분석하고 싶었고, 워드 클라우드를 사용하기로 결정했다. 
그리하여 내가 수집한 다양한 기사들에서 가장 많이 사용된 단어들을 수집하여 워드 클라우드로 나타낼 수 있었다.

---

# 📝 프로젝트 내용

### | 주제

인공지능 또는 AI는 인간의 학습능력, 추론능력, 지각능력을 인공적으로 구현하려는 컴퓨터 과학의 세부분야 중 하나이다. 정보공학 분야에 있어 하나의 인프라 기술이기도 하다.컴퓨터는 과거의 유사한 행동 사례를 통해 얻은 광범위한 데이터를 사용하여 인간의 행동을 ‘모방’하도록 프로그래밍되고 고양이와 새의 차이를 인식하는 것부터 제조 시설에서 복잡한 활동을 수행하는 것에 이르기까지 다양하다.

---

# 📝 프로젝트 내용

### | 교과 연관성

해당 주제는 독서 과목의 주장하는 글쓰기 수행평가와 연관된다.

---

# 📝 프로젝트 내용

### | 활동 내용

ai주제와 관련된 최근 기사들을 txt파일로 정리하여 수집하고 특정 모양의 워드 클라우드로 나타냄

---

## 💡 code

- #### import modules

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
```

---

## 💡 code

- #### read data

```python
with open('C:/Users/User/OneDrive/바탕 화면/python_lesson-main/word_cloud/project.txt', 'r', encoding='utf-8') as f:
    text = f.read()

okt = Okt()
nouns = okt.nouns(text) # 명사만 추출

words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함

```

---

## 💡 code

- #### read data

```python
img = Image.open('C:/Users/User/OneDrive/바탕 화면/python_lesson-main/word_cloud/temp.jpg')
img_array = np.array(img)

wc = WordCloud(font_path='malgun', width=251, height=201, scale=2.0, max_font_size=250, mask=img_array)
gen = wc.generate_from_frequencies(c)

wc.to_file("a.png")

plt.figure()
plt.imshow(gen)
```

---

## ✅ result

![](./a.png)