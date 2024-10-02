import sqlite3
import csv



connection = sqlite3.connect("hr.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees 
                (Emp_ID INT, Name TEXT, Position TEXT)''')

file = open('population_data.csv')
city_data.csv.reader(file)
city_data.__next__()
cursor.executemany('''INSERT INTO Employees VALUES (?, ?, ?)''', city_data)


connection.commit()
connection.close()
