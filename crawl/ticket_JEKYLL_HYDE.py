import requests
from bs4 import BeautifulSoup
import ticket_module as tm

session = requests.session()



url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemainFN"

headers = {
    "Referer": "http://ticket.yes24.com/OSIF/Book.asmx?op=GetHallMapRemainFN",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

params = {
    'idHall': '8531',
    'idTime': '971101'
}

res = session.post(url, data=params, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

seat_info1 = soup.find('regend').get_text()
seat_info2 = soup.find('section').get_text()


tm.split_1(seat_info1)
print("---------")
tm.split_2(seat_info2)
