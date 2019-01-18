import openpyxl
from pprint import pprint

book = openpyxl.load_workbook("/Users/lhj/images/melon_top100.xlsx")

sheet = book.worksheets[0]

data = []
for r in sheet.rows:
    data.append([ r[0].value, r[1].value, r[3].value ])

del data[0]    # header 제거
del data[0]

data = sorted(data, key=lambda x: x[2], reverse=True)

pprint(data)

