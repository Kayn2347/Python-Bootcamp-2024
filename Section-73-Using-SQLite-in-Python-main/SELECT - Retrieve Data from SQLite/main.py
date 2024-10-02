import sqlite3

connection = sqlite3.connect("hr.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees 
                (Emp_ID INT, Name TEXT, Position TEXT)''')



cursor.execute('''SELECT * FROM Population''')
print(cursor.fetchone())
#print(results)
for row in results:
    print(row)

connection.commit()
connection.close()
