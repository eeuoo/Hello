import urllib.request as ur

url = "http://www.weather.go.kr/repositary/image/rdr/img/RDR_CMP_WRC_201901081305.png"

saveFile = "/Users/lhj/images/test1.png"
mem = ur.urlopen(url).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")

