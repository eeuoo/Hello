from bs4 import BeautifulSoup
import requests
import urllib.parse as parse
import os.path as path
import urls



url = "https://blog.naver.com/PostView.nhn?blogId=korea_diary&logNo=221433346994&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fwww.naver.com%2F&directAccess=false"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

sel = "img.se-image-resource"

imgs = soup.select(sel)
# print(imgs, len(imgs))

if len(imgs) < 1 :
    exit()

img = imgs[0]
src = img.get('src')
print('img>>>', src)

for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open ("/Users/lhj/images/" + urls.getFilename(src), "wb") as file :
        file.write(requests.get(src).content)

