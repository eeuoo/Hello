from apiclient.discovery import build
from pymongo import MongoClient, DESCENDING
from pprint import pprint
from googleapiclient.errors import HttpError
import time


API_KEY = "AIzaSyA_ww16Zva6Htex1KXy29rw3Rpx7uloCKk"  #본인의 API키

def get_youtube(q):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    req = youtube.search().list(
        part='snippet',
        q=q,
        type='video',
        maxResults = 2
    )

    i = 0
    while req and i < 2 :
        search_res = req.execute()
        
        results = search_res['items']

        ids = [ item['id']['videoId'] for item in results ]

        ssResult = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(ids)
        ).execute()

        yield ssResult['items']

        req = youtube.search().list_next(req, search_res)

        i += 1



def insert_mongo(data):
    mongo_client = MongoClient('localhost', 27017)

    collection = mongo_client.doodb.Youtubes  # connection

    mongo_result = collection.insert_many(data)  

    print('Affected docs is {}'.format(len(mongo_result.inserted_ids)))


def top10():

    mongo_client = MongoClient('localhost', 27017)

    collection = mongo_client.doodb.Youtubes  # connection

    lst = collection.find().sort("viewCount",DESCENDING).limit(10)

    for i in lst:
        pprint(i)
 
def viewCount_int(youtubes):
    for i, y in enumerate(youtubes):
      print(y) 
        

if __name__ == "__main__":  

    try:
        youtubes = get_youtube('파이썬')

        viewCount_int(youtubes)

    except HttpError as err:
    # If the error is a rate limit or connection error,
    # wait and try again.

        if err.resp.status in [403, 500, 503]:
            print("error!!!")
            time.sleep(5)
        else: raise


    
