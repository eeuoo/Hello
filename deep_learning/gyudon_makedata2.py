from PIL import Image
import os, glob
import numpy as np
import random, math

# 분류 대상 카테고리
root_dit = './data/'
categories = ['normal', 'beni', 'negi', 'cheese']
nb_classes = len(categories)
image_size = 50

# 이미지 데이터 읽어 들이기
X = []   # 이미지 데이터
Y = []   # 레이블 데이터
def add_sample(cat, fname, is_train) :
    img = Image.open(fname)
    img = img.convert('RGB')   # 색상 모드 변경
    img = img.resize( (image_size, image_size) )   # 이미지 크기 변경
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)

    if not is_train :
        return
    
    # 각도를 조금 변경한 파일 추가하기
    # 회전하기
    for ang in range(-20, 20, 5) :
        img2 = img.rotate(ang)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)

        img2.save('gyudon_' + str(ang) + '.PNG')

        # 반전하기
        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)

