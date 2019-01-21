import csv, codecs
import openpyxl

fp = codecs.open("./crawl/melon_top100.csv", "r", "utf-8")

reader = csv.reader(fp, delimiter=',', quotechar='"')

book = openpyxl.Workbook()
sheet1 = book.active
sheet1.title = "melon top100"


for i, row in enumerate(reader):
    #  print(i, row)
   for j, col in enumerate(row):
       tcell = sheet1.cell(row=(i+1), column=j+1)

       if i > 0 and (j == 0 or j > 2) and col.isnumeric():
           tcell.number_format
           tcell.value = int(col)
       else:
           tcell.value = col

# 저장하기
book.save("./crawl/melon_top100.xlsx")