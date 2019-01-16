from bs4 import BeautifulSoup
import requests

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

xml = requests.get(url).text

soup = BeautifulSoup(xml, 'html.parser')

seq0 = soup.select("data[seq='0']")

for d in soup.select('body data'):
    seq = d.attr['seq']
    ws = d.find('ws')
    wdkor = d.find('wdkor')
    print(seq, ws, wdkor)