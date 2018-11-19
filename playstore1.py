from bs4 import BeautifulSoup
import requests
# from requests import get
from Game import Game

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select("div.card-list")
# print(card_list)

print(">>>>>>>", len(card_list), type(card_list[0]))

games = []

for i in card_list:
    cards = i.select('div.card')
    print("OOOOO>>>>", len(cards))
    for c in cards:
        games.append(Game(c))

for i in games:
     print(i)

with open("games.csv", "w", encoding = 'utf-8') as file:
        file.write("게임명\t제조사\n")
        for i in games:
                file.write(i + "\n")     