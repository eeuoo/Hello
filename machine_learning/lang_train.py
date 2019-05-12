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


# 각 파일 처리
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)

    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return { "freqs" : freqs, "labels" : labels }

data = load_files("./lang/train/*.txt") # 학습 데이터
test = load_files("./lang/test/*.txt")  # 검증 데이터


# json으로 결과 저장
with open("./lang/freq.json", "w", encoding="utf-8") as fp :
    json.dump([data, test], fp)

# 학습
clf = svm.SVC()
clf.fit( data["freqs"], data["labels"] )

# 예측
predict = clf.predict( test["freqs"] )

# 결과 테스트
ac_score = metrics.accuracy_score( test["labels"]. predict )
cl_report = metrics.classification_report( test["labels"], predict )

print( "정답률= ", ac_score )
print( "리포트= ", cl_report)