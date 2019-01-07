int_numbers = range(-5, 6)
print("int_numbers", list(int_numbers))

negatives = filter(lambda x: x < 0, int_numbers)
print("negatives", list(negatives))

# lambda x: x < 0
# = def fn(x):
#     return x < 0

na = filter(lambda x : x % 2 == 0, int_numbers)
print("na", list(na))

ne = filter(lambda x : x % 2 == 1, int_numbers)
print("ne", list(ne))

ni = filter(lambda x : x * 2, int_numbers)
print("ni", list(ni))

def filter(l):
    ret = []
    for i in l:
        if i == True:
           print("ret", ret.append(i))

