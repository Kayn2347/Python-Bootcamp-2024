from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference


spreadsheet = Workbook()
sheet = spreadsheet.active
rows = [
    ["Book Name", "Paperback", "Ebook"],
    ["DSA Swift", 40, 55],
    ["DSA Java", 50, 40],
    ["DSA Python", 45, 30],
    ["Python for Kids", 55, 35],
    ["Scratch", 35, 30],
]

for row in rows:
    sheet.append(row)

chart = BarChart()
data = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=6,
                 min_col=2,
                 max_col=3)
chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "E2")
cats = Reference(worksheet=sheet,
                 min_row=2,
                 max_row=6,
                 min_col=1,
                 max_col=1)
chart.set_categories(cats)
spreadsheet.save("sample_charts.xlsx")