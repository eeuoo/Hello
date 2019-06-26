from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
import numpy as np

image_w = 28
image_h = 28
nb_classes = 10

def main() :
    # 폰트 이미지 데이터 읽기
    xy = np.load('./data/font_draw.npz')
    X = xy['x']
    Y = xy['y']

    # 데이터 정규화하기
    X = X.reshape(X.shape[0], image_w * image_h).astype('float32')
    X /= 255
    Y = np_utils.to_categorical(Y, 10)

    # 학습 전용 데이터와 테스트 전용 데이터 나누기
    X_train, X_test, y_train, y_test = train_test_split(X, Y)

    # 모델 구축하기
    model = build_model()
    model.fit(X_train, y_train,
        batch_size = 128, nb_epoch = 20, verbose = 1,
        validation_data = (X_test, y_test)) 

    # 모델 저장하기
    model.save_weights('font_draw.hdf5')
