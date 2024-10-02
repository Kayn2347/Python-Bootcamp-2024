import sqlite3



connection = sqlite3.connect("hr.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees 
                (Emp_ID INT, Name TEXT, Position TEXT)''')

employess = [(1, 'Kayn', 'Student'),
             (2, 'Dhea', 'Developer'),
             (3, 'Chisee', 'Sales'),

cursor.executemany('''INSERT INTO Employees VALUES (?, ?, ?)''', employess


connection.commit()
connection.close()
