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
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a")
    code_z = ord("z")

    # 알파벳 출현 횟수 구하기
    for ch in text :
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n - code_a] += 1

    
    # 정규화
    total = sum(cnt)
    freq = list(map(lambda n : n / total, cnt))
    return (freq, lang)


