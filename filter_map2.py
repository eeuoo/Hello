int_numbers = range(-5,6)

f = filter(lambda x : x < 0, int_numbers)
m = map(lambda x : x < 0, int_numbers)

print(list(f))
print(list(m))

f2 = filter(lambda x : x * 2, int_numbers)
m2 = map(lambda x : x * 2, int_numbers)

print(list(f2))
print(list(m2))
