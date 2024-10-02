import sqlite3

connection = sqlite3.connect("hr.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTSE Employees 
                (Emp_ID INT, Name TEXT, Position TEXT)''')


employees = [(1, 'Kayn', 'Instructor'),
            (2, 'Dhea', 'Developer'),
            (3, 'Chisee', 'Sales')]


name ='Kayn'

cursor.execute('''delete from Employees where name=?''', (name,))
connection.commit()
connection.close()
