from bs4 import BeautifulSoup
import requests

url = "https://t1.daumcdn.net/movie/178a154b50fc44798e963bf9612e90c61543371406503"

img = requests.get(url).content

saveFile = "/Users/lhj/images/test4.png"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("OK!")
