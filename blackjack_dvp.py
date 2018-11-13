class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class Deck:
    
    def randomcard():
        import random
        deck_all = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']
        deck1 = ['s','c','h','d']
        deck2 = [2,3,4,5,6,7,8,9,10,'a','j','k','q']
                # a == 1 or a == 10
                # j == 10
                # k == 10
                # q == 10 으로 계산


class Game:
    while (cardsum < 21):     
        def start_game(self):
            card = Deck.randomcard(deck)

            cardlist = []
            cardlist.append(card)

            cardsum = int(cardlist[0]) + int(cardlist[1]) +  ...


class Player(Game):
   
    if cardsum == 21:
        print("승")

    elif cardsum > 21:
        print("패")

    elif cardsum < 21:

        hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")
        
        if hitorstand == '1':
            continue

        elif hitorstand == '2':
            break
    
    pcs = return (cardsum)


class Dealer:

    def reveal():
        print(card1)
        
    if cardsum > 17:
        break
    
    dcs = return (cardsum)


if dcs < pcs:
     print("승")

elif dcs > pcs:
    print("패")
