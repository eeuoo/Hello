import requests, json
from bs4 import BeautifulSoup
from pprint import pprint 
from PIL import Image
import openpyxl

url = "https://www.melon.com/chart/index.htm"

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')
trs1 = soup.select('tr[data-song-no]')

book = openpyxl.load_workbook("crawl/melon_top100.xlsx")
sheet2 = book.create_sheet()
sheet2.title = "두번째 시트"


for index, i in enumerate(trs1) :
    i = i.select(' a img ')[0]
    i = i.attrs['src']

    fileName = 'melon_img' + str(index+1) + '.png'
    
    f = open ("/Users/lhj/images/" + fileName, "wb") 
    
    f.write(requests.get(i).content)

    f.close()

    imgFile = '/Users/lhj/images/' +  fileName

    img2 = Image.open(imgFile)

    new_img = img2.resize((100, 100))
    new_img.save(imgFile)
    img3 = openpyxl.drawing.image.Image(imgFile)
    sheet_num = 'A' + str(index + 1)
    sheet2.add_image( img3, sheet_num)
    sheet2.row_dimensions[index+1].height = 80
    sheet2.column_dimensions['A'].width = 15

book.save("crawl/melon_top100.xlsx")

