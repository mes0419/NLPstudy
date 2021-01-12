'''
4.8 분절 복원
python 4.8.py 4.8.input.txt
공백에 ▁를 추가 -> ▁ ▁  2개가 됨  -> ▁ ▁  를 공백으로 치환 -> 한 개 ▁ 만 남음 -> 마지막으로 지움
자연어 처리는 인공지능의 한 줄기 입니다
▁자연 어 ▁처 리는 ▁인 공 지 능 의 ▁한 ▁줄 기 ▁입니다 : 서브워드 분절
▁자연▁어▁▁처▁리는▁▁인▁공▁지▁능▁의▁▁한▁▁줄▁기▁▁입니다
▁자연▁어 처▁리는 인▁공▁지▁능▁의 한 줄▁기 입니다
자연어 처리는 인공지능의 한 줄기 입니다
'''


import sys

STR = '▁'

if __name__ == "__main__":
    ref_fn ='4.8.input.txt'#sys.argv[1]

    #f = open(ref_fn, 'r')
    f = open(ref_fn, 'r', encoding='UTF-8')
    for ref in f:
        ref_tokens = ref.strip().split(' ')
        input_line = sys.stdin.readline().strip()
        if input_line != "":
            tokens = input_line.split(' ')

            idx = 0
            buf = []

            # We assume that stdin has more tokens than reference input.
            for ref_token in ref_tokens:
                tmp_buf = []

                while idx < len(tokens):
                    if tokens[idx].strip() == '':
                        idx += 1
                        continue

                    tmp_buf += [tokens[idx]]
                    idx += 1

                    if ''.join(tmp_buf) == ref_token:
                        break

                if len(tmp_buf) > 0:
                    buf += [STR + tmp_buf[0].strip()] + tmp_buf[1:]

            sys.stdout.write(' '.join(buf) + '\n')
        else:
            sys.stdout.write('\n')

    f.close()