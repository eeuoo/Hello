# idHall과 idTime 가져오기

import requests
from bs4 import BeautifulSoup


session = requests.session()


def login_page(perfUrl, session):


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


    #접근할 페이지 1
    res = session.get(perfUrl)
    rs = res.raise_for_status()



url = 'http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx?IdPerf=32149'

login_page(url, session)