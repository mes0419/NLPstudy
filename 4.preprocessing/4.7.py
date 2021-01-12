'''
4.7 서브워드 분절
BPE : byte pair encoding (Mecab은 형태소 분석기)
https://shwksl101.github.io/nlp/2019/08/11/Konlpy_BPE.html
구글의 sentencepiece 사용 가능(아래 url)
 https://keep-steady.tistory.com/7
 https://lsjsj92.tistory.com/600
Unknown Token에 효율적인 대처 가능
Transformer, BERT 들도 서브워드 분절 방식
 pip install sentencepiece
 '''

import sentencepiece as spm
'''
input_file = 'ratings_train.txt'
vocab_size = 5000
model_name = 'bpe_test'
model_type = 'bpe'
user_defined_symbols = '[PAD],[UNK],[CLS],[SEP],[MASK],[UNK1],[UNK2],[UNK3],[UNK4],[UNK5]'

input_argument = '--input=%s --model_prefix=%s --vocab_size=%s --user_defined_symbols=%s --model_type=%s'
cmd = input_argument%(input_file, model_name, vocab_size,user_defined_symbols, model_type)
spm.SentencePieceTrainer.Train(cmd)
'''

sp = spm.SentencePieceProcessor()
sp.Load("bpe_test.model")
print(sp.EncodeAsPieces("자연어 처리는 인공지능의 한 줄기 입니다"))
'''
['▁자연', '어', '▁처', '리는', '▁인', '공', '지', '능', '의', '▁한', '▁줄', '기', '▁입니다']
▁ <--- bpe 적용에 따른 분리랑 구분 짓기 위해 원래 띄어쓰기는 ▁를 사용한다. _ 랑 다른 특수문자 
'''
