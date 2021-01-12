# 4.4 문장 단위 분절
# 4.4.1 문장 단위 분절 예제

import sys, fileinput, re
from nltk.tokenize import sent_tokenize
import nltk

#nltk.download('punkt')
'''
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

# 4.4.2 문장 합치기 및 분절 예제
'''
if __name__ == '__main__':
    buf = []
    for line in fileinput.input():
        if line.strip() != "":
            buf += [line.strip()]
            sentences = sent_tokenize(" ".join(buf))

            if len(sentences) > 1:
                buf = sentences[1:]

                #sys.stdout.write('\n'.join(sentences[0]) + '\n')
                sys.stdout.write(sentences[0] + '\n')
    #이 다음줄로 안넘어감..
    sys.stdout.write(" ".join(buf) + "\n")
