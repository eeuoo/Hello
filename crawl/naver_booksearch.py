import requests
from bs4 import BeautifulSoup

url = ""

title = "python"
params = {
    "query" : title,
    "display" : 20,
    "start" : 1,
    "sort" : "date" ,
    "headers" : 
}

headers = {
    "X-naver-Client_id"
}


result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(resul)

print()