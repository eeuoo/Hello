from functools import reduce

lst = [1, 2, 3, 4]
product = lst[0]
for i,num in  enumerate(lst):
    if i == 0 : continue
    product = product * num

print("product1>>", product)

product2 = reduce(lambda x, y : x * y, lst)
print("product2>>", product2)

    