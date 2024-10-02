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
new_data = data.groupby("country", sort=False)["popu"].sum()
city_count = data.groupby("country")["name"].count()
print(city_count)
