import urllib.request as ur


url = " http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm={}&endTm={}"

def inputDate (yy, mm, dd):
    return (yy-mm-dd)


saveFile = "/Users/lhj/images/2018_earthquake_volcano2.html"
mem = ur.urlopen(url).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")
