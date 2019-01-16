import requests, json
from bs4 import BeautifulSoup
import re

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "h8D7yhnqUBsVaCHQOViJ",
    "X-Naver-Client-Secret": "TYwzilDXGl"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

print(json.dumps(jsonData, ensure_ascii=False, indent=2))


for item in jsonData["items"]:

    print(item['title'] ,item['bloggerlink'], item['bloggername'], item['postdate'])

