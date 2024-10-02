from openpyxl.utils import FORMULAE
from openpyxl import load_workbook


spreadsheet = load_workbook("sample_data.xlsx")
sheet = spreadsheet.active
sheet["C2"] = "Total"
sheet["D2"] = "=SUM(B2:B100)"
sheet["C3"] = "Average"
sheet["D3"] = "=AVERAGE(B2:B100)"
sheet["C4"] = "More than 80"
sheet["D4"] = 'COUNTIF(B2:B100, ">80")'
spreadsheet.save("sample_data.xlsx")