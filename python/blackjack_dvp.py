import random

class Deck:

    def card():
        deck_m = ['heart', 'spade', 'diamond', 'clover']
        deck_s = ['a',2,3,4,5,6,7,8,9,10,'q','k','j']
                         
        return [random.choice(deck_m), random.choice(deck_s)]

class Card:

    def start_cardlist(self):
       cardlist = []
        
        # while(len(self.cardlist) < 2):
       self.cardlist = cardlist.append( Deck.card() )
       print(self.cardlist)    
            
       

ss = Card()
ss.start_cardlist()