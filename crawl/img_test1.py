import urllib.request as ur

url = "http://blogfiles.naver.net/20111005_168/woosam8502_13177752820979P6LC_JPEG/%BB%E7%B7%C1%B4%CF%BD%A3%B1%E60003.JPG"

saveFile = "/Users/lhj/images/test2.jpg"
ur.urlretrieve(url, saveFile)
print("OK!")
