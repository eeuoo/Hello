from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

csv = pd.read_csv('./data/iris.csv')

cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)

clf = svm.SVC(gamma='auto')  
clf.fit(trainData, trainLabel)   # training

print(trainData.shape)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)    # test

print("pred >> ", pred)
print("score >> ", score)

r =  clf.predict([[5.4,3.9,1.7,0.4]])
print('품종은 Iris-setosa인가 ?', r[0])

