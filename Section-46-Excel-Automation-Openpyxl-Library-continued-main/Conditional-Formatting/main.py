
from openpyxl.formatting.rule import DataBarRule
from openpyxl import load_workbook


spreadsheet = load_workbook("sample_data.xlsx")
sheet = spreadsheet.active
data_bar_rule = DataBarRule(start_type="num",
                            start_value=60,
                            end_type="num",
                            end_value=100,
                            color="0000FF00")
sheet.conditional_formatting.add("B2:B100", data_bar_rule)
spreadsheet.save("sample_data2.xlsx")

