from bs4 import BeautifulSoup
import requests
import urls

url = "http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32059"
html = requests.get(url).text
soup = BeautifulSoup( html, 'html.parser')

headers = { "referer" : "http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=32059"}

img = requests.get(url, headers=headers)
aaa = soup.find(img,'ulSeatSpace' ).text

print(aaa)
