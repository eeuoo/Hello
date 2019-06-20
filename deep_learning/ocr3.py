import sys
import numpy as np
import cv2
import ocr_mnist

# MNIST 학습 데이터 읽어 들이기
mnist = ocr_mnist.build_model()
mnist.load_weights('mnist,hdf5')
