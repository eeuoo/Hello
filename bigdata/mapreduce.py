
samples = [
    (2001, 23),
    (2002, 7),
    (2002, -12),
    (2001, 21),
    (2003, 20),
    (2005, 13),
    (2003, 3),
    (2005, -2),
    (2003, 22),
    (2001, -3),
]

dic = {}

for data in samples:
    if data[0] not in dic.keys() :
        dic[data[0]]=[data[1]]
    else :    
        dic[data[0]].append(data[1])

print(dic)

dic2 = {}

for data in samples:
    try:
        dic2[data[0]].append(data[1])
    except KeyError :
        dic2[data[0]] = [data[1]]


print(dic2)

print("---------------result")

for i in dic.items():
    print(i[0],max(i[1]))

# 실행결과
# { 2001: [-3, 21, 23],
#   2002: [-12, 7],
#   2003: [3, 20, 22],
#   2005: [-2, 13] }
# ---------------------------------- result
# 2001	23
# 2002	7
# 2003	22
# 2005	13
