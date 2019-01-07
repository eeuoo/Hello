내 답안

i, sum = 0, 0
while (i>=0 and i < 100)
    i = i + 1
    if(i % 2 == 0):
        continue

    sum = sum + i
    if (i == 99):
        print(sum)
        break    


선생님 답압

i, sum = 0, 0
while(i < 100):
    i = i + 1
    if (i % 2 == 1):
     sum = sum + i

print(sum)