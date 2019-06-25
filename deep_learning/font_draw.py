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

# 회전하거나 확대해서 데이터 늘리기
def gen_image(base_im, no, font_name) :
    for ang in range(-20, 20, 2) :
        sub_im = base_im.rotate(ang)
        data = np.asarray(sub_im)
        X.append(data)
        Y.append(no)
        w = image_size

        # 조금씩 확대하기
        for r in range(8, 15, 3) :
            size = round( (r/10) * image_size )
            im2 = cv2.resize( data, (size, size), cv2.INTER_AREA )
            data2 = np.asarray(im2)

            if image_size > size :
                x = (image_size - size) // 2
                data = np.zeros( (image_size, image_size) )
                data[x : x+size, x : x+size] = data2
            
            else :
                x = (size - image_size) // 2
                data = data2[x : x+w, x : x+w]
            
            X.append(data)
            Y.append(no)

            if random.randint(0, 400) == 0 :
                fname = "image/num/n-{0}-{1}-{2}.PNG".format( font_name, no, ang, r )
                cv2.imwrite(fname, data)

# 이미지 렌더링
X = []
Y = []

for path in ttf_list :
    font_name = os.path.basename(path)

    try :
        fo = ImageFont.truetype(path, size=100)
    except :
        continue

    for no in range(10) :
        im = Image.new('L', (200, 200))
        draw_text(im, fo, str(no))

        
