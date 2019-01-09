from bs4 import BeautifulSoup
import requests
import urls

url = "https://finance.naver.com/marketindex/"
html = requests.get(url).text
soup = BeautifulSoup( html, 'html.parser')

iframe = 'iframe#frame_ex1'
ifsoup = soup.select_one(iframe)
ifsrc = ifsoup.get('src')

joinUrl = urls.urljoin( urls.getHostname(url, True), ifsrc)
joinHtml = requests.get(joinUrl).text
joinSoup = BeautifulSoup(joinHtml, 'html.parser')


source_len_tr = joinSoup.select('body > div > table > tbody > tr')
real_len = len(source_len_tr)

tr_sel = 'body > div > table > tbody > tr'
trs = joinSoup.select(tr_sel)

finance = []

print(" 국가  /  살 때  /  팔 때   /  환율차이 ")

for tr in trs :

    nation = tr.select('td')[0].text.split()[0]
    buy = tr.select('td')[1].text
    sell = tr.select('td')[2].text

    buy = buy.replace(',', '')
    sell = sell.replace(',','')

    dif = round( (float(buy) - float(sell)), 2 )
    
    a = "{} , {} , {} , {}".format(nation, buy, sell, dif)

    print(a)