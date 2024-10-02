# with open("sales.csv") as file:
#      result = file.read().split('\n')
#      print(result)


lines = (line fo line in open("sales.csv"))
split_lines = (s.rstrip().split(",") for s in lines)
columns = next(split_lines)
company_dicts = (dict(zip(columns, data)) for data in split_lines)
sales_amount = (int(company_dict["SaleAnt"]) for company_dict in company_dicts)
total_sales = sum(sales_amount)
print(f"Total sales Amount ${total_sales}")
