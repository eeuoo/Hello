import urllib.request as ur
import timeit
start = timeit.default_timer()

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

saveFile = "/Users/lhj/images/weather.html"

data = ur.urlopen(url).read()
text = data.decode('utf-8')

with open (saveFile, mode="w") as file :
    file.write(text)

print("OK!", (timeit.default_timer() - start) * 1000)
