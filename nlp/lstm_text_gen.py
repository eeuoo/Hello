import codecs
from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

fp = codecs.open('./BEXX0003.txt', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one('body')
text = body.getText() + " "
print('코퍼스의 길이 : ', len(text))

# 문자를 하나하나 읽어 들이고 ID 붙이기
chars = sorted( list(set(text)) )
print( '사용되고 있는 문자의 수 : ', len(chars) )
char_indices = dict( (c,i) for i , c in enumerate(chars) )    # 문자 > ID
indices_char  = dict( (i,c) for i, c in enumerate(chars) )    # ID > 문자

# 텍스트를 maxlen개의 문자로 자르고 다음에 오는 문자 등록하기
maxlen = 20
step = 3
sentences = []
next_chars = []

for i in range(0, len(text) - maxlen, step) :
    sentences.append( text[i: i + maxlen] )
    next_chars.append( text[i + maxlen] )

print('학습할 구문의 수 : ', len(sentences) )
print('텍스트를 ID 벡터로 변환합니다....')

X = np.zeros( len(sentences), maxlen, len(chars), dtype = np.bool )
y = np.zeros( len(sentences), len(chars), dtype =  np.bool )

for i, sentence in enumerate(sentences) :
    for t, char in enumerate(sentence) :
        X[ i, t, char_indices[char] ] = 1
    
    y[ i, char_indices[next_chars[i]] ] = 1

# 모델 구축하기(LSTM)
print('모델을 구축합니다.....')
model = Sequential()
model.add( LSTM( 128, input_shape = (maxlen, len(chars)) ) )
model.add( Dense(len(chars)) )
model.add( Activation('softmax') )
optimizer = RMSprop(lr = 0.01)
model.compile(loss = 'categorical_crossentropy', optimizer = optimizer)