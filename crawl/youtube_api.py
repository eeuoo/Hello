from apiclient.discovery import build
from pymongo import MongoClient, DESCENDING
from pprint import pprint
from googleapiclient.errors import HttpError
import time


API_KEY = "AIzaSyA_ww16Zva6Htex1KXy29rw3Rpx7uloCKk"  #본인의 API키


def main():

    # youtubes = get_youtube('파이썬')

    # one = viewCount_int(youtubes)

    mongo_client = MongoClient('localhost', 27017)

    collection = mongo_client.doodb.Youtubes  # connection

    # insert_mongo(collection, one)

    top10(collection)


def get_youtube(q):

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    req = youtube.search().list(
        part='snippet',
        q=q,
        type='video',
        maxResults = 50
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

        time.sleep(3)


def insert_mongo(collection, data):
    
    mongo_result = collection.insert_many(data)  

    print('Affected docs is {}'.format(len(mongo_result.inserted_ids)))


def top10(collection):

    lst = collection.find().sort("statistics.viewCount",DESCENDING).limit(10)

    for i in lst:
        print( 'title ::', i['snippet']['title'], 'viewCount >>>', i['statistics']['viewCount'] )
 

def viewCount_int(youtubes):
  
    for yous in youtubes:
        for vc in yous:
            for i, s in vc['statistics'].items():
                vc['statistics'][i] = int(s)
                
            yield vc

         
if __name__ == "__main__":  

    try:
        main()

    except HttpError as err:
    # If the error is a rate limit or connection error,
    # wait and try again.

        if err.resp.status in [403, 500, 503]:
            print("error!!!")
            time.sleep(5)
        else: raise


    
