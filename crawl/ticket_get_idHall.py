import requests
from bs4 import BeautifulSoup


session = requests.session()


url = "https://www.yes24.com/Templates/FTLogin.aspx?ReturnURL=http://ticket.yes24.com/Pages/Perf/Detail/DetailSpecial.aspx&&ReturnParams=IdPerf=32098"

headers =  { "Referer" : url }

params = {
    "SMemberID" : "dlguswn512" ,
    "SMemberPassword" : "lhzoo4295"
 }

res = session.post(url, data = params, headers = headers)
res.raise_for_status()

res2 = session.get('http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098')
res.raise_for_status()

soup = BeautifulSoup(res2.text, "html.parser")

print(soup)
exit()

script = soup.find('ul#ulTime')

print(script)

