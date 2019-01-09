import sys
import requests

API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
params = {
    "stdId": regionNumber
}

content = requests.get(API, params=params).text
xml = content.decode('utf-8')