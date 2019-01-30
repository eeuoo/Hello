import requests, json
from bs4 import BeautifulSoup
from pprint import pprint 
from PIL import Image
import openpyxl


url = "https://www.instagram.com/kim_bora95/?hl=ko"

headers = {
'referer' : 'https://www.instagram.com/kim_bora95/',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' 
}


html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')

trs1 = soup.select('section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(3) > a > div.eLAPa > div.KL4Bh')



for i in trs1 :

    # i = i.attrs['src']

    print(i)

    # fileName = 'melon_img' + str(index+1) + '.png'
    
    # f = open ("/Users/lhj/images/" + fileName, "wb") 
    
    # f.write(requests.get(i).content)

    # f.close()