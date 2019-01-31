from pymongo import MongoClient, DESCENDING
import requests, json
from bs4 import BeautifulSoup
from pprint import pprint


def get_api(page=1):
    url = "https://openapi.naver.com/v1/search/book.json"

    title = "파이썬"
    params = {
        "query": title,
        "display": 100,
        "start": page,
        "sort": "date"
    }

    headers = {
        "X-Naver-Client-Id": "h8D7yhnqUBsVaCHQOViJ",
        "X-Naver-Client-Secret": "TYwzilDXGl"
    }

    result = requests.get(url, params=params, headers=headers).text

    jsonData = json.loads(result)
    jsonData = jsonData['items']

    # print(json.dumps(jsonData, ensure_ascii=False, indent=2))



def insert_mongo():
    mongo_client = MongoClient('localhost', 27017)

    collection = mongo_client.doodb.Books  # connection

    # mongo_result = collection.insert_many(jsonData)  

    # print('Affected docs is {}'.format(len(mongo_result.inserted_ids)))

    lst = collection.find().sort("price",DESCENDING).limit(5)

    for i in lst:
        pprint(i)

if __name__ == "__main__":
    insert_mongo()