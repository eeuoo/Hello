import requests, json
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

jsonUrl = "https://www.melon.com/commonlike/getSongLike.json?contsIds=31554349%2C31554317%2C31532643%2C31532438%2C31477685%2C31406357%2C31417871%2C31506637%2C31448480%2C31388145%2C31492319%2C31403163%2C30962526%2C31373277%2C31455159%2C31399721%2C31495659%2C31453551%2C31266290%2C31314144%2C31346009%2C31542508%2C31402611%2C31304766%2C31356458%2C31417922%2C31151836%2C31316695%2C31062863%2C31433084%2C31532642%2C31340985%2C31388213%2C31085237%2C31144690%2C31526249%2C30244931%2C31403156%2C30699142%2C31492321%2C31470006%2C31510409%2C31266289%2C31492322%2C31131273%2C31286161%2C30637982%2C31399726%2C31551385%2C31133898%2C31314142%2C31399725%2C30568338%2C31266282%2C31399728%2C31331745%2C3087601%2C31175119%2C31344113%2C31302310%2C31085238%2C31457611%2C31399724%2C30806536%2C31399731%2C31486544%2C30314784%2C31399730%2C30809895%2C31399727%2C31399729%2C31266291%2C8235260%2C31399722%2C31478848%2C30672529%2C30725482%2C31553909%2C30669593%2C31219546%2C30859584%2C31266288%2C31551382%2C31541154%2C30960341%2C31356799%2C30717645%2C31113240%2C30884950%2C31356451%2C31539246%2C31433086%2C31085244%2C31433089%2C31460625%2C31433085%2C31532644%2C31496140%2C31266286%2C31433087%2C31399795"


headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

jsonHeaders = { 'Referer': 'https://www.melon.com/chart/index.htm',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')
trs1 = soup.select('#lst50')
trs2 = soup.select('#lst100')

jsonHtml = requests.get(jsonUrl, headers=jsonHeaders)
jsonData = json.loads(jsonHtml.text)
# songInfo = json.dumps(jsonData, ensure_ascii=False, indent=2)



dic = {}

def get_list (trs) :
        
    for td in trs:
        
        dataSongNo = td.attrs['data-song-no']
        rank = td.select('td:nth-child(2) > div > span.rank')[0].text
        name = td.select('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')[0].text
        artist = td.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
        likeCnt = ''

        if len(artist) > 2 :
            artistList = []
            for i in artist :
                artistList.append(i.text)
            artist = artistList
        else : artist = artist[0].text

        tempDic = {'rank' : rank, "CONTSID": dataSongNo, "name": name , "artist" : artist, "likeCnt" : likeCnt}

        dic[dataSongNo] = tempDic


get_list(trs1)
get_list(trs2)



for j in jsonData['contsLike']:
    songId = str(j['CONTSID'])
    x = dic.get(songId)
    if x == None :
        continue
    x['likeCnt'] = j['SUMMCNT']


for i in dic.values() :
    print("{}위 {} - {}  ♡ {}".format(i['rank'], i['name'], i['artist'], i['likeCnt']))