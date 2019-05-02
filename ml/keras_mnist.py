from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils import np_utils

# data 준비
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 28 * 28).astype('float32')
X_test = X_test.reshape(10000, 28 * 28).astype('float32')

X_train = X_train / 255
X_test = X_test / 255

# label 범주화
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# 학습모델 정의
model = Sequential()

# Layer1
model.add(Dense(512, input_shape=(784, )))
model.add(Activation('relu'))
model.add(Dropout(0.2))

# Layer2
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10))
model.add(Activation('softmax'))

# model compile(구축하기)
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# training
hist = model.fit(X_train, y_train)

# test
score = model.evaluate(X_test, y_test, verbose=1)
print('loss =', score[0])
print('accuracy =', score[1])
