import random

deck_m = ['heart', 'spade', 'diamond', 'clover']
deck_s = ['a',2,3,4,5,6,7,8,9,10,'q','k','j']

cardlist = []

while(len(cardlist) <= 2):
    card = [random.choice(deck_m), random.choice(deck_s)]
    cardlist.append( card )

    print(cardlist)

input_msg = input ("hit or stand (hit : 1, stand : 2 -->")

if input_msg == '1' :
    card = [random.choice(deck_m), random.choice(deck_s)]
    cardlist.append( card )
    print(cardlist)

elif input_msg == '2':
    for i in range(cardlist):
        cardsum = 0
        cardsum = cardsum + cardlist[i][1]
        print(cardsum)    