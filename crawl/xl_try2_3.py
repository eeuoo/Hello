'''상위 Top10의 `좋아요 수`는 BarChart로, 
  `좋아요 차이 수`는 ScatterChart로 세번째 시트에 작성하시오.'''

import openpyxl
from openpyxl.chart import ( Reference, BarChart )
from openpyxl.chart import ( Reference, Series, ScatterChart )


book = openpyxl.load_workbook("crawl/melon_top100.xlsx")
sheet1 = book.worksheets[0]
sheet3 = book.create_sheet()
sheet3.title = "세번째 시트"


# BarChart

datax = Reference(sheet1, min_col=4, 
		min_row=2, max_col=4, max_row=11)
categs = Reference(sheet1, min_col=2, max_col=2,
				 min_row=2, max_row=11)

chart1 = BarChart()
chart1.add_data(data=datax)
chart1.set_categories(categs)

chart1.legend = None  # 범례
chart1.varyColors = True
chart1.title = "Top10 좋아요 수"

sheet3.add_chart(chart1, "A2")



# ScatterChart

chart2 = ScatterChart()
chart2.style = 13
chart2.x_axis.title = '곡'
chart2.y_axis.title = '좋아요 차이'

chart2.title = "Top10 좋아요 수"

xvalues = Reference(sheet1, min_col=1, max_col=1,
				 min_row=1, max_row=11 )

values = Reference(sheet1, min_col=5, max_col=5,
				min_row=2, max_row=11)

series = Series(values, xvalues, 
				title_from_data=True)

chart2.series.append(series)

sheet3.add_chart(chart2, "A14")


book.save("crawl/melon_top100.xlsx")

