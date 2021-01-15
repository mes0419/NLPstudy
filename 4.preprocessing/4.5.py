#4.5.1 한국어 분절
#mecab 설치 필요
#https://velog.io/@kjyggg/%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EA%B8%B0-Mecab-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-A-to-Z%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EB%8B%A8%EC%96%B4-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%EB%93%B1%EB%A1%9D%EA%B9%8C%EC%A7%80
#https://eunjeon.blogspot.com/2013/02/blog-post.html
#pip install eunjeon

#mecab은 속도가 제일 빠름
from eunjeon import Mecab
m = Mecab()
print(m.pos("안녕하세요, 반갑습니다"))
print(m.morphs("안녕하세요, 반갑습니다")) #형태소 분리 <- wakati
print(m.nouns("안녕하세요, 반갑습니다")) #명사 분리

'''morphs
https://pypi.org/project/mecab-python3/
wakati는 없는 듯
wakati = Mecab.Tagger("-Owakati")
print(wakati.parse("안녕하세요, 반갑습니다"))
'''

#4.5.2 영어 분절
#Moses -> 최신 버젼은 사용할 필요 없음
import sys, fileinput
from nltk.tokenize import word_tokenize
print(word_tokenize("Don't you know that? Mizy's ice cream store has moved."))

#중국어 분절 skip