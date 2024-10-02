from openpyxl import Workbook


new_workbook = Workbook()
sheet = new_workbook.active
sheet["A1"] = "name"
sheet["B1"] = "surname"

sheet.insert_row(idx=1, amount=7)
sheet.delete_rows(idx=1, amount=7)
sheet.delete_rows(idx=1)
new_workbook.save("new_spreadsheet.xlsx:")

for row in sheet.iter_rows(values_only=True)
print(row)
