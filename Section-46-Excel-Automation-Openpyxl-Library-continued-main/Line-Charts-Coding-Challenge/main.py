# TODO1 - Generate custom data and save it to Excel - the data will be generated randomly for each month 
from openpyxl import Workbook
import random
from openpyxl.chart import line_chart, Reference



spreadsheet = Workbook()
sheet = spreadsheet.active

rows =[
    ["", "January, February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  ["Paperback", ],
  ["Ebook", ],
]
for row in rows:
    sheet.append(row)

for row in sheet.iter_rows(min_row=2,
                           max_row=3,
                           min_col=2,
                           max_col=13):
    for cell in rows:
        cell.value = random.randrange(10, 100)
  
# - TODO2 - Create line graph
chart = LineChart()
data = Reference(worksheet=sheet,
                 min_row=2,
                 max_row=3,
                 min_col=1,
                 max_col=13)
chart.add_data(data, from_rows=True, titles_from_data=True)
sheet.add_chart(chart, "C6")
# TODO 3 - Create category for the graph
cats = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=1,
                 min_col=2,
                 max_col=13)
chart.set_categories(cats)


spreadsheet.save("line_chart.xlsx")


