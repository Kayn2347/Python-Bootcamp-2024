import names
from openpyxl import Workbook


spreadsheet = Workbook()
sheet = spreadsheet.active
sheet["A1"] = "Full Name"
sheet["B1"] = "Score"
spreadsheet.save("sample_data.xlsx")

for i in range(100):
  print(names.get_full_name())