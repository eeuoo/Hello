def gen() :
    for i in range(10):
        yield i ** 3

for i in gen():
    print(i)

    
for i in range(10):
     print(i**3)