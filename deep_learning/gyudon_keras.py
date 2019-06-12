from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np

# 분류 대상 카테고리
root_dir = './data/'
categories = ['normal', 'beni', 'negi', 'cheese']