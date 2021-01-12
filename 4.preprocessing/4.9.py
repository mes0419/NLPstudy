'''
4.9 토치텍스트
한 줄에서 클래스와 텍스트가 tab 으로 구분된 데이터의 입력을 받는 내용 -> 텍스트 분류
https://github.com/kh-kim/simple-ntc

한 라인이 텍스트로만 채워져 있을 때를 위한 코드 -> 언어 모델
https://github.com/kh-kim/OpenNLMTK

텍스트로만 채워진 두개의 파일을 동시에 입력데이터로 읽어들이는 코드 -> 기계번역, 요약
https://github.com/kh-kim/simple-nmt

https://wikidocs.net/65348
https://torchtext.readthedocs.io/en/latest/data.html#torchtext.data.Field
'''

from torchtext import data
from eunjeon import Mecab

tokenizer = Mecab()

'''
use_vocab – Whether to use a Vocab object. If False, the data in this field should already be numerical. Default: True.
lower – Whether to lowercase the text in this field. Default: False.
batch_first – Whether to produce tensors with the batch dimension first. Default: False.
batch_first : 미니 배치 차원을 맨 앞으로 하여 데이터를 불러올 것인지 여부. (False가 기본값)
fix_length – A fixed length that all examples using this field will be padded to, or None for flexible sequence lengths. Default: None.
#최대허용길이 설정해 패딩작업
https://wikidocs.net/65794
is_target – Whether this field is a target variable. Affects iteration over batches. Default: False
'''
ID = data.Field(sequential=False,
              use_vocab=False)

TEXT = data.Field(sequential=True,
                  use_vocab=True,
                  tokenize=tokenizer.morphs, # 토크나이저로는 Mecab 사용.
                  lower=True,
                  batch_first=True,
                  fix_length=20)

LABEL = data.Field(sequential=False,
                   use_vocab=False,
                   is_target=True)

from torchtext.data import TabularDataset
train_data, test_data = TabularDataset.splits(
        path='.', train='ratings_train.txt', test='ratings_test.txt', format='tsv',
        fields=[('id', ID), ('text', TEXT), ('label', LABEL)], skip_header=True)

print('훈련 샘플의 개수 : {}'.format(len(train_data)))
print('테스트 샘플의 개수 : {}'.format(len(test_data)))

print(vars(train_data[0]))

TEXT.build_vocab(train_data, min_freq=10, max_size=10000)
print('단어 집합의 크기 : {}'.format(len(TEXT.vocab)))
print(TEXT.vocab.stoi)


from torchtext.data import Iterator
batch_size = 5
train_loader = Iterator(dataset=train_data, batch_size = batch_size)
test_loader = Iterator(dataset=test_data, batch_size = batch_size)

print('훈련 데이터의 미니 배치 수 : {}'.format(len(train_loader)))
print('테스트 데이터의 미니 배치 수 : {}'.format(len(test_loader)))

batch = next(iter(train_loader)) # 첫번째 미니배치
print(batch.text)

