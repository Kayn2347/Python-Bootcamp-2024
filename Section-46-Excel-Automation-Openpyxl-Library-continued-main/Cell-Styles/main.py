from openpyxl.styles import Font,Color, Alignment, Border,Side
from openpyxl import load_workbook
from openpyxl.styles import NamedStyle


spreadsheet = load_workbook("sample_data.xlsx")
sheet = spreadsheet.active
header = NamedStyle(name="header")
header.font = Font(bold=True, size=17)
header.alignment = Alignment(horizontal="center", vertical="center")
first_row = sheet[1]
for cell in first_row:
    cell.style = header



spreadsheet.save("sample_data.xlsx")