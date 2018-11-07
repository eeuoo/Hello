x = (1,2,3,5,7)
y, sumx, sumy = 9, 18, 0

while(y < 99):
    y = y + 2
    if(y % 3 != 0 and y % 5 != 0 and y % 7 != 0):
     sumy = sumy + y

print(sumx + sumy)