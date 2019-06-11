import sys, os, re, time
import urllib.request as req
import urllib.parse as parse
import json

# API의 URL 지정하기
PHOTOZOU_API = 'https://api.photozou.jp/rest/search_public.json'
CACHE_DIR = './data/cache'

# 포토주 API로 이미지 검색하기
def search_photo(keyword, offset = 0, limit = 100) :
    # API 쿼리 조합하기
    keyword_enc = parse.quote_plus(keyword)
    q = 'keyword={0}&offset={1}&limit={2}'.format(keyword_enc, offset, limit)
    url = PHOTOZOU_API + '?' + q

    # 캐시 전용 폴더 만들기
    if not os.path.exists(CACHE_DIR) :
        os.makedirs(CACHE_DIR)
    
    cache = CACHE_DIR + '/' + re.sub(r'[^a-zA-Z0-9\%\#]+', '_', url)
    
    if os.path.exists(cache) :
        return json.load( open(cache, 'r', encoding='utf-8') )

    print('[API] ' + url)

    req.urlretrieve(url, cache)
    time.sleep(1)     # 1초 쉬기

    return json.load( open(cache, 'r', encoding='utf-8') )
    