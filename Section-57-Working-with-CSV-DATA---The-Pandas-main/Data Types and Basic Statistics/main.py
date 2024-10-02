import pandas


pandas.set_option("display.max.rows", None)
pandas.set_option("display.float_format", str)
data = pandas.read_csv("population_data.csv")
basic_statistics = data.describe()
print(basic_statistics)
