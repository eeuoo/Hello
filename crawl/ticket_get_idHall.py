import requests
from bs4 import BeautifulSoup


session = requests.session()


url = "http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098"

headers =  { "Referer" : "http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32098" 
}

# params = {
#     "SMemeberID" : "dlguswn512" ,
#     "SMemeberPassword" : "lhzoo4295"
# }

res = session.post(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
print(soup)
exit()
script = soup.find('ul#ulTime')

print(script)

