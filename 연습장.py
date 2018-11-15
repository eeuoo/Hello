import random
from functools import reduce

class Deck:
    
    def randomcard():
        deck = ['s2','s3','s4','s5','s6','s7','s8','s9','s10','c2','c3','c4','c5','c6','c7','c8','c9','c10','h2','h3','h4','h5','h6','h7','h8','h9','h10','d2','d3','d4','d5','d6','d7','d8','d9','d10']
        
        return random.choice(deck)

class Game:
     
    def start_game(self):
       cardsum = 0 
       while (cardsum < 21):  
        if cardsum < 21:  
            card = Deck.randomcard()
            
            cardlist = list.append(card)

            print(cardlist)

            numlist = []
            numlist.append(int(card[1]))

            cardsum = reduce(lambda x, y : x + y, numlist) 

        if cardsum >= 21: 
            print(cardsum)
            break   
          
game = Game()
game.start_game()
        