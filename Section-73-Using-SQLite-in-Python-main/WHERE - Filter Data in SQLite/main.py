import sqlite3

connection = sqlite3.connect("hr.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Population 
                (City TEXT, Country TEXT, Pop_Number INT)''')


# cursor.execute('''SELECT * FROM Population''')
# print(cursor.fetchone())
# #print(results)
# for row in results:
#     print(row)
country = 'Spain'
pop = 1000000

cursor.execute('''Select * from Population where Country=? and Pop_Number>''', ('Italy', 1000000))
print(cursor.fetchall())



connection.commit()
connection.close()
