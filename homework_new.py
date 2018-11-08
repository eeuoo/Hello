sum = 2

for n in range(2,101):
    
    for i in range(2,n):
       
        if ( n % i == 0):
            break
       
        if i == (n-1):
            sum = sum + n

print(sum)
