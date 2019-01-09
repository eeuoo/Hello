from bs4 import BeautifulSoup
import requests
import urls



bbsUrl = "https://blog.naver.com/korea_diary/221433346994"
html = requests.get(bbsUrl).text
soup = BeautifulSoup(html, 'html.parser')

ifrSel = 'iframe#mainFrame'
ifr = soup.select_one(ifrSel)
src = ifr.get('src')
orgUrl = urls.urljoin( urls.getHostname(bbsUrl, True), src )

orgHtml = requests.get(orgUrl).text
orgSoup = BeautifulSoup(orgHtml, 'html.parser')

titleSel = "div.se-title-text span"
title = orgSoup.select_one(titleSel).text

sel = "img.se-image-resource"
imgs = orgSoup.select(sel)

if len(imgs) < 1 :
    exit()

img = imgs[0]
src = img.get('src')
print('img>>>', src)

print('---------------', title,'---------------')
for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open ("/Users/lhj/images/" + urls.getFilename(src), "wb") as file :
        file.write(requests.get(src).content)

