from sklearn import svm, metrics
import glob, os.path, re, json

# 텍스트 읽어 출현 빈도 조사
def check_freq():
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, "r", encoding='utf-8') as f:
        text = f.read()
    text = text.lower()

    # 숫자 세기 변수 초기화
