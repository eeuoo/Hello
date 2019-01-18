# idHall과 idTime 가져오기

import requests
from bs4 import BeautifulSoup
import re
import ticket_module as tm
import page2 


def get_idperf (URL) :
    try : 
        pIdPerf = re.findall("IdPerf=(.*)&", URL)[0]
    except IndexError:
        pIdPerf = re.findall("IdPerf=(.*)", URL)[0]
    
    return pIdPerf


session = requests.session()

loginUrl = "https://www.yes24.com/Templates/FTLogin.aspx"

headers = {
    "Referer": 'http://ticket.yes24.com/',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

login_info = {
        'LoginType': '',
        'FBLoginSub$ReturnURL': 'http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx' ,
        'FBLoginSub$ReturnParams': 'IdPerf=32098' ,
        'RefererUrl': '', 
        'AutoLogin': '1' ,
        'LoginIDSave': 'Y' ,
        'FBLoginSub$NaverCode': '' ,
        'FBLoginSub$NaverState': '' ,
        'FBLoginSub$Facebook': '' ,
        'SMemberID': 'dlguswn512' ,
        'SMemberPassword': 'qlalf123'
}

res = session.post(loginUrl, data=login_info, headers=headers)
res.raise_for_status()
 
perfUrl = 'http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32149'


#접근할 페이지 1
res = session.get(perfUrl)
res.raise_for_status()



#접근할 페이지 2

page2_headers = { 'Referer': perfUrl,
'Host': 'ticket.yes24.com',
'Origin': 'http://ticket.yes24.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

pid = get_idperf(perfUrl)

page2_params = {
    "pIdPerf": pid ,
    'pIdCode': '' ,
    'pIsMania': '0'
}

res2 =  session.post('http://ticket.yes24.com/Pages/Perf/Sale/Ajax/Perf/PerfFlashDateAll.aspx',headers=page2_headers, data=page2_params)

res2.raise_for_status()


#idHall과 idTime 추출
soup2 = BeautifulSoup(res2.text, "html.parser")


pDay = soup2.select('option[value]')

pDayList = []

for i in pDay : 
   pDayList.append(i.attrs['value'].replace('-',''))




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

        


    #접근할 페이지 4

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




