from sklearn import svm, metrics
import pandas as pd
from sklearn.externals import joblib
from pathlib import Path
from sklearn.model_selection import GridSearchCV

def readCsv(file, maxcnt):
    labels = []
    images = []
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i >= maxcnt:
                break
            cols = line.split(",")
            labels.append(int(cols.pop(0)))      # 첫번째 자리가 label
            images.append(list(map(lambda b: int(b) / 256, cols)))  # 실수 벡터화
    return {"labels": labels, "images": images}


test = readCsv('./data/t10k.csv', 10000)

# print(test['images'])
pklFile = "./data/mnist.pkl"
clf = None
if Path(pklFile).exists():              # from pathlib import Path
    print("File Exists!!")
    clf = joblib.load(pklFile)

# training ---------------------------
if not clf:
    train = readCsv('./data/train.csv', 60000)   # 학습용 데이터가 많아질수록 스코어 상승!
    clf = svm.SVC(gamma='auto')
    print(len(train['labels']))
    clf.fit(train['images'], train['labels'])
    joblib.dump(clf, pklFile)

# test -------------------------
pred = clf.predict(test['images'])

score = metrics.accuracy_score(test['labels'], pred)
print("\n\nscore=", score)

report = metrics.classification_report(test['labels'], pred)
print(report)