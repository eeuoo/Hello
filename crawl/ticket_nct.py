import requests
from bs4 import BeautifulSoup
import ticket_JEKYLL_HYDE as tjk

session = requests.session()



#url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemain"
url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemainFN"

headers = {
    "Referer": "http://ticket.yes24.com/OSIF/Book.asmx?op=GetHallMapRemainFN",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

params = {
    'idHall': '8531',
    'idTime': '985109'
}

res = session.post(url, data=params, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

seat_info = soup.find('regend').get_text()
seat_info2 = soup.find('section').get_text()

seat_list = seat_info.split('^')

real_seat_list = []

for i in seat_list :
    sl = i.split('@')
    real_seat_list.append(sl)

#print(real_seat_list)

for j, k in enumerate(real_seat_list):
    
    if real_seat_list[j][0] == '' :
        continue
    else :
        aa = real_seat_list[j][4] + ' ' + real_seat_list[j][2] + '원' + " " + real_seat_list[j][3] + '석'

    print(aa)

tjk.split_2(seat_info2)
