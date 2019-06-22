import os, glob
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2, random

# 크기 지정하기
image_size = 28   # MNIST와 같은 크기

# 폰트 설정하기
ttf_list = glob.glob('/Library/Fonts/*.ttf')
ttf_list += glob.glob('~/Library/Fonts/*.ttf')

# 중앙에 문자 그리기
def draw_text(im, font, text) :
    dr = ImageDraw.Draw(im)
    im_sz = np.array(im.size)
    fo_sz = np.array(font.getsize(text))
    xy = (im_sz - fo_sz) / 2

    print(im_sz, fo_sz)

    dr.text(xy, text, font = font, fill = (255) )


# 샘플 이미지를 출력할 폴더
if not os.path.exists('./image/num') :
    os.makedires('./image/num')
    