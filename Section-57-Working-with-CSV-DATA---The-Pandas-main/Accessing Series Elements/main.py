import pandas


pandas.set_option("display.max.rows", None)
pandas.set_option("display.float_format", str)
data = pandas.read_csv("population_data.csv")
population = pandas.Series([1000, 2000, 500],
                           index=["London", "Berlin", "Tokyo"])
revenue = pandas.Series({"London": 10000, "Berlin": 2030304})
# print(type(data["name"]))
colors = pandas.Series(["blue", "green", "yellow", "red", "purple"],
                       index=[1, 2, 4, 6, 8])
print(colors.loc[-1])

