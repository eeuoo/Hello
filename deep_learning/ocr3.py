import sys
import numpy as np
import cv2
import ocr_mnist

# MNIST 학습 데이터 읽어 들이기
mnist = ocr_mnist.build_model()
mnist.load_weights('mnist,hdf5')

# 이미지 읽어 들이기
im = cv2.imread('numbers100.PNG')

# 윤곽 추출하기
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)   # 그레이 스케일로 변환
blur = cv2.GaussianBlur(gray, (5,5), 0)  # 블러
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)  # 2진화
cv2.imwrite('numbers100-th.PNG', thresh)
contours = cv2.findContours(thresh,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

# 추출한 좌표 정렬하기
rects = []
im_w = im.shape[1]
for i, cnt in enumerate(contours) :
    x, y, w, h = cv2.boundingRect(cnt)
    
    if w < 10 or h < 10 :
        continue   # 너무 작으면 생략하기

    if w > im_w / 5 :
        continue   # 너무 크면 생략하기

    y2 = round(y / 10) * 10   # y좌표 맞추기
    index = y2 * im_w + x
    rects.append( (index, x, y, w, h) )

rects = sorted(rects, key = lambda x : x[0])   # 정렬하기

