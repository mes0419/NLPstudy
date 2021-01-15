# 4.4 문장 단위 분절
# 4.4.1 문장 단위 분절 예제
# python 4.4.1.py 4.4.1.input.txt

import sys, fileinput, re
from nltk.tokenize import sent_tokenize
import nltk

#nltk.download('punkt')

if __name__ == "__main__":
     for line in fileinput.input():
         #line.strip : 양쪽 공백 제거
         if line.strip() != "":
             line = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', line.strip())
             #sent_tokenize : 문장의 시작과 끝을 구분
             sentences = sent_tokenize(line.strip())

             for s in sentences:
                 if s != "":
                     sys.stdout.write(s+"\n")

