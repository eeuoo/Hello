# idHall과 idTime 가져오기

import requests
from bs4 import BeautifulSoup
import re
import ticket_module as tm
import page1, page2, page4


def get_idperf (URL) :
    try : 
        pIdPerf = re.findall("IdPerf=(.*)&", URL)[0]
    except IndexError:
        pIdPerf = re.findall("IdPerf=(.*)", URL)[0]
    
    return pIdPerf


perfUrl = 'http://ticket.yes24.com/Pages/Perf/Detail/Detail.aspx?IdPerf=31656'

session = requests.session()



#접근할 페이지 1 (로그인 페이지) (import page1)
page1.login_page(perfUrl, session)



#접근할 페이지 2 (import page2)
pDayList = page2.get_pDay(perfUrl, session)

pid = get_idperf(perfUrl)


#접근할 페이지 3 
page3_headers = { 'Referer': perfUrl ,
"X-Requested-With" : "XMLHttpRequest",
'Host': 'ticket.yes24.com',
'Origin': 'http://ticket.yes24.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


#공연 날짜마다의 잔여 좌석수

for day in pDayList:

    page3_params = {
        'pDay': day,
        'pIdPerf': pid,
        'pIdCode': '', 
        'pIsMania': '0'
    }

    res3 =  session.post('http://ticket.yes24.com/Pages/Perf/Sale/Ajax/Perf/PerfTime.aspx',headers=page3_headers, data=page3_params)
    res3.raise_for_status()



    #idHall과 idTime 추출
    soup3 = BeautifulSoup(res3.text, "html.parser")

    idHall = soup3.select_one('ul#ulTimeData >li').attrs['idhall']
    idTime = soup3.select_one('ul#ulTimeData >li').attrs['value']


    #접근할 페이지4 (import page4)
    page4.get_seats(session, idHall, idTime, day)




# ToDo : 콘서트 / 뮤지컬 / 공연 잔여좌석수 나타내는 패턴 만들기

