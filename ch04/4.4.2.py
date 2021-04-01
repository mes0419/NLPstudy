# 4.4 문장 단위 분절
# 4.4.2 문장 합치기 및 분절 예제
# python 4.4.2.py 4.4.2.input.txt

import sys, fileinput, re
from nltk.tokenize import sent_tokenize
import nltk

#nltk.download('punkt')

if __name__ == '__main__':
    buf = []
    for line in fileinput.input():
        if line.strip() != "":
            buf += [line.strip()]
            sentences = sent_tokenize(" ".join(buf))

            if len(sentences) > 1:
                buf = sentences[-1:]

                sys.stdout.write('\n'.join(sentences[:-1]) + '\n')
    #이 다음줄로 안넘어감..
    sys.stdout.write(" ".join(buf) + "\n")
