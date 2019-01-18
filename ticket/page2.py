#접근할 페이지 2 - pDay 추출하기

import requests
from bs4 import BeautifulSoup
import re

url = "http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098"

# pIdPerf = re.findall("IdPerf=(.*)", url)[0]

def get_idperf (perfUrl) :

    pIdPerf = re.findall("IdPerf=(.*)&", perfUrl)[0]

    return pIdPerf


def get_pDay(perfUrl):

    session = requests.session()
        
    page2_headers = { 'Referer': perfUrl ,
    'Host': 'ticket.yes24.com',
    'Origin': 'http://ticket.yes24.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    # 공연 url 받아서 공연번호(Idperf) 추출
    
    idperf = get_idperf(perfUrl)


    # 공연 url 받아서 공연번호 뽑아서 params에 pIdPerf에 넣기

    page2_params = {
        "pIdPerf": idperf ,
        'pIdCode': '' ,
        'pIsMania': '0'
    }

    res =  session.post('http://ticket.yes24.com/Pages/Perf/Sale/Ajax/Perf/PerfFlashDateAll.aspx',headers=page2_headers, data=page2_params)

    res.raise_for_status()


    pDayList = []

    # pDay 추출
    soup2 = BeautifulSoup(res.text, "html.parser")

    pDay = soup2.select('option[value]')

    
    for i in pDay : 
        pDayList.append(i.attrs['value'].replace('-',''))

        
    return pDayList
