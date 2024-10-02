from openpyxl import load_workbook
import names, random


workbook = load_workbook("new_spreadsheet.xlsx")
sheet = workbook.active
sheet["A1"] = "Full Name"
sheet["B1"] = "Score"
for i in range(2, 101):
    sheet["A"+str(i)] = names.get_full_name()
    sheet["B"+str(i)] = random.randint(60, 100)
workbook.save("new_spreadsheet.xlsx")



