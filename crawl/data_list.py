import random
from pprint import pprint

data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}



sum_dic = {}

for key in data.keys():
    aa=0
    bb=0

    for i in range(0, len(data['A'])):
        a = data[key][i][i]
        aa += a

        b = data[key][i][-1-i]
        bb += b

    sum = aa + bb

    sum_dic[key] = sum


min_s = min(sum_dic.values())


# 방법 1
for key, sum in sum_dic.items():
    if sum == min_s:
        print (key)

# 방법 2
print(min(sum_dic, key=lambda k : sum_dic[k]))

# 방법 3
print((min(sum_dic.items(), key=lambda x : x[1])[0]))

# 방법 4
vk = dict((v,k) for k,v in sum_dic.items())
print(vk[min_s])

# 방법 5
mk = ''
mv = 100000
for k, v in sum_dic.items():
    if v < mv :
        mk = k
        mv = v

print(mk)


