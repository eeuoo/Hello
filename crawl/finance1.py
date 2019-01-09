from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

usd = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
# usd = soup.select_one('#exchangeList span.value').text

print("usd=", usd, float(usd.replace(',', '')))