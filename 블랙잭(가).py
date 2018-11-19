import random

deck_m = ['heart', 'spade', 'diamond', 'clover']
deck_s = ['a',2,3,4,5,6,7,8,9,10,'q','k','j']

cardlist = []

while(len(cardlist) < 2):
   card = [random.choice(deck_m), random.choice(deck_s)]
   cardlist.append( card )

   print(cardlist)

   cardsum = 0

while(cardsum <= 21):

   input_msg = input ("hit or stand (hit : 1, stand : 2 -->")


   if input_msg == '1' :
       card = [random.choice(deck_m), random.choice(deck_s)]
       cardlist.append( card )
       print(cardlist)
       for i in cardlist:
        #    while 넣어서 문제 4번 해결할 것
           if (i[1]) == 'a':
               input_a = input("a를 1로 하겠습니까? -> 1입력 아니면 11로 하겠습니까? -> 11입력")
               if input_a == '11' or input_a == '1':
                   i[1] = int(input_a)
               else :
                   print("다시입력하세요")

           elif (i[1]) == "q" or (i[1]) == "k" or (i[1]) == "j":
               i[1] = 10

           cardsum = cardsum + i[1]
           
       continue

   elif input_msg == '2':
       
       for i in cardlist:

           if (i[1]) == 'a':
               input_a = input("a를 1로 하겠습니까? -> 1입력 아니면 11로 하겠습니까? -> 11입력")
               
               if input_a == '11' or input_a == '1':
                   i[1] = int(input_a)
               else :
                   print("다시입력하세요")

           elif (i[1]) == "q" or (i[1]) == "k" or (i[1]) == "j":
               i[1] = 10

           cardsum = cardsum + i[1]
           
       
       break

print(cardsum)       