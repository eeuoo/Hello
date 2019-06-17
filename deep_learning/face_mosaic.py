import cv2, sys, re

# 입력 파일 지정하기
if len(sys.argv) <= 1 :
    print("no input file")
    quit()

image_file = sys.argv[1]

# 출력 파일 이름
output_file = re.sub( r'\,jpg|jpeg|PNG$', '_mosaic.jpg', image_file)
mosaic_rate = 30

# 캐스캐이드 파일 경로 지정하기
cascade_file = "haarcascade_frontalface_alt.xml"

# 이미지 읽어 들이기
image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환

