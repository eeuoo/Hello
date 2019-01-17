# idHall과 idTime 가져오기

import requests
from bs4 import BeautifulSoup
import ticket_pDay_module as tday
import ticket_idperf_module as tid

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
        'SMemberPassword': 'lhzoo4295'
}

res = session.post(loginUrl, data=login_info, headers=headers)
res.raise_for_status()
 

#접근할 페이지 1
res = session.get('http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098')
res.raise_for_status()



#접근할 페이지 3

perfUrl = 'http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098' 

page2_headers = { 'Referer': perfUrl ,
"X-Requested-With" : "XMLHttpRequest",
'Host': 'ticket.yes24.com',
'Origin': 'http://ticket.yes24.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


# ToDo 공연마다 회차정보(날짜) 받아서 pDay에 넣기
# ToDo 공연마다 회차정보(공연번호) 받아서 pIdPerf에 넣기

perfid = tid.get_idperf(perfUrl)
perfdays = tday.get_pDay(perfUrl)
print(perfid)
print(perfdays)

page2_params = {
    'pDay': perfdays,
    'pIdPerf': perfid,
    'pIdCode': '', 
    'pIsMania': '0'
}

res =  session.post('http://ticket.yes24.com/Pages/Perf/Sale/Ajax/Perf/PerfTime.aspx',headers=page2_headers, data=page2_params)
res.raise_for_status()




#idHall과 idTime 추출
soup2 = BeautifulSoup(res.text, "html.parser")

idHall = soup2.select_one('ul#ulTimeData >li').attrs['idhall']
idTime = soup2.select_one('ul#ulTimeData >li').attrs['value']

print("idHall" ,idHall)
print("idTime", idTime)


