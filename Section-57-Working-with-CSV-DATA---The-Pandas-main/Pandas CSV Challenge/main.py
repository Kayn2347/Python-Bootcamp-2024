import pandas as pd


pd.set_option('display.max_rows', None)
data = pd.read_csv("Sales.csv")
print("Original data frame")
print(data)
data_agg = data.groupby(['customer_id','salesman_id']).agg({'amount':['sum','count']})
print("Aggregated data frame")
print(data_agg)
data_agg.to_csv("Sales_agg.csv")
