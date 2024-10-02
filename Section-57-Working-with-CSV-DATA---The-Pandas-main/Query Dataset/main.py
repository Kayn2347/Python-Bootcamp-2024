import pandas


# pandas.set_option("display.max.rows", None)
# pandas.set_option("display.float_format", str)
# data = pandas.read_csv("population_data.csv")
# population = pandas.Series([1000, 2000, 500],
#                            index=["London", "Berlin", "Tokyo"])
# office_count = pandas.Series([10, 20],
#                              index=["London", "Berlin"])

# city_data = pandas.DataFrame({"population": population,
#                              "office_count" : office_count})
# print(data.[city_data.office_count.notna()])
new_data = data[data.country == "Germany"]
not_null_data = data[data.popu.notnull()]
cities_withA= data[data.name.str.starswith("Al")]
cities_with_end = data[data.name.str.endswith("e")]
new_cities_data = data[(data.name.str.endswith("e")) & (data.country == "Germany")]
cities_spain = data[(data.popu > 500000) & (data.country == "Spain")]
average_pop = int(data["popu"].mean())
cities_france = data[(data.popu > average_pop) & (data.country == "France")]
print(cities_france)
