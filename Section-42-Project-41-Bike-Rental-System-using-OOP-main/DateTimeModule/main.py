import datetime as dt


date_string = "28 September, 2024"
date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print(date_object)
