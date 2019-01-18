import requests
from bs4 import BeautifulSoup
import ticket_module as tm


#접근할 페이지 4

def get_seats(session,idHall, idTime, day):

    url = "http://ticket.yes24.com/OSIF/Book.asmx/GetHallMapRemainFN"

    headers4 = {
        "Referer": "http://ticket.yes24.com/OSIF/Book.asmx?op=GetHallMapRemainFN",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    params4 = {
        'idHall': idHall,
        'idTime': idTime
    }

    res4 = session.post(url, data=params4, headers=headers4)
    res4.raise_for_status()

    soup4 = BeautifulSoup(res4.text, "html.parser")

    seat_info = soup4.find('regend').get_text()
    seat_info2 = soup4.find('section').get_text()

    print('공연일자', day[0:4],'년',day[4:6],'월',day[6:8],'일')
    tm.split_1(seat_info)
    print("-------------------")
    tm.split_2(seat_info2)
    print("**************")