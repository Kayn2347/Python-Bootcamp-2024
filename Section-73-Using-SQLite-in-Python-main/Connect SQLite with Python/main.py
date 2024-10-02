import sqlite3

connection = sqlite3.connect("hr.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees 
                (Emp_ID INT, Name TEXT, Position TEXT)''')
connection.commit()
connection.close()
