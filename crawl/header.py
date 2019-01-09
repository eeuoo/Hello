import requests

url = "https://dthumb-phinf.pstatic.net/?type=f156_156&src=%22https://image-comic.pstatic.net/mobilewebimg/651664/187/9e368c2c01331c69aacf1efd5c4fe762_003.jpg%22"

headers = { "referer" : "https://comic.naver.com/webtoon/detail.nhn?titleId=651664&no=187&weekday=fri"}

saveFile = '/Users/lhj/images/comic_test.png' 
mem = requests.get(url, headers=headers).content
with open( saveFile, mode="wb") as file :
    file.write(mem)

print("OK!!")