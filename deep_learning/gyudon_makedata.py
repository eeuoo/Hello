from sklearn import model_selection
from sklearn.model_selection import train_test_split
from PIL import Image
import os, glob
import numpy as np

# 분류 대상 카테고리
root_dir = './data/'
categories = ['normal', 'beni', 'negi', 'cheese']
nb_classes = len(categories)
image_size = 50

# 폴더마다의 이미지 데이터 읽어 들이기
X = []    # 이미지 데이터
Y = []    # 레이블 데이터
