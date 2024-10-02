# with open("population_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv

# with open("populaion_data.csv") as data_file:
#      data = csv.reader(data_file)
#      population = []
#      for row in data:
#          print(row)

import pandas

data = pandas.read_csv("population_data.csv")
print(data["pop"])
