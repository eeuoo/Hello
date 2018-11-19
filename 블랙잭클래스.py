import random

class Deck:

    def card():
        deck_m = ['heart', 'spade', 'diamond', 'clover']
        deck_s = ['a',2,3,4,5,6,7,8,9,10,'q','k','j']
        
        card = [random.choice(deck_m), random.choice(deck_s)]
        
        return card
        

class Card:

    def start_cardlist(self):
        while(len(cardlist) < 2):
        
        self.card = Deck.card()
        
        cardlist = []
        self.cardlist = cardlist.append( self.card )

        print(self.cardlist)

        

    def cardsum(self):
            
            cardsum = 0

            for i in self.cardlist:

                if (i[1]) == 'a':
                    input_a = input("a를 1로 하겠습니까? -> 1입력 아니면 11로 하겠습니까? -> 11입력")
                    if input_a == '11' or input_a == '1':
                        i[1] = int(input_a)
                    else :
                        print("다시입력하세요")

                elif (i[1]) == "q" or (i[1]) == "k" or (i[1]) == "j":
                    i[1] = 10

                self.cardsum = self.cardsum + i[1]          

class Player:

input_msg = input ("hit or stand (hit : 1, stand : 2 -->")

class Dealer:


