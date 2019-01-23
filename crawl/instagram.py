import requests, json
from bs4 import BeautifulSoup
from pprint import pprint 
from PIL import Image
import openpyxl


url = 'https://www.instagram.com/graphql/query/?query_hash=e6a78c2942f1370ea50e04c9a45ebc44&variables=%7B%22id%22%3A%224732410085%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFCVDdiU192NWhMYjBvM2hfSzVrRUUzS09uMFVEaVZfaEhSdU9HUWp4Q1o4YWZfRjhjQmVWbm9ocmk5MzFBa0xDajB3VjVKMUdLVVFzM3dYX25XUS1mVw%3D%3D%22%7D'

headers = {
'referer' : 'https://www.instagram.com/kim_bora95/',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' 
}


html = requests.get(url, headers=headers)

print(html)
soup = BeautifulSoup(html.text, 'html.parser')

# print(soup)
trs1 = soup.select('div.KL4Bh > img')

#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div.KL4Bh

for i in trs1 :

    # i = i.attrs['src']

    print(i)

    # fileName = 'melon_img' + str(index+1) + '.png'
    
    # f = open ("/Users/lhj/images/" + fileName, "wb") 
    
    # f.write(requests.get(i).content)

    # f.close()