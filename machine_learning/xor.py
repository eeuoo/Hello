from sklearn import svm, metrics
import pandas as pd

xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

df = pd.DataFrame(xor_data)

clf = svm.SVC(gamma='auto')
clf.fit(df.loc[:, 0:1], df.loc[:, 2])

testset1 = [[0,1]]
testset2 = [[0, 1], [1, 0], [1, 1], [2, -1], [3, 1]]

pred = clf.predict(testset2)
score = metrics.accuracy_score([1, 1, 0, 1, 0], pred)

print('pred = ', pred)
print('score = ', score)

while True :
    cmd = input("x y 값 입력 >>")
    if not cmd : break
    x, y = cmd.split(' ')
    t = [[int(x), int(y)]]
    p = clf.predict(t)[0]
    print("pred = ", "참" if p == 1 else '거짓')


# print(df.loc[:, 0:1])
# print('-------')
# print(df.loc[:,2])

# print('head = ', df.head)
# print('shape = ', df.shape)
# print('cols = ', list(df.columns))
# print('index = ', len(df.index))


