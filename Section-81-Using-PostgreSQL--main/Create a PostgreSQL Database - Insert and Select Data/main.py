import pyscopg


connection = pyscopg.connect(dbname='hr',
                            user='postgres',
                             password='123456',
                             host='localhost',
                             port='5432')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXIST EMP
                  (ID INT PRIMARY KEY,
                  FIRST_NAME TEXT,
                  LAST_NAME TEXT,
                  EMAIL TEXT,
                  POSISTION TEXT);''')

new_emp = (1002, 'Kayn', 'Lourence', 'kaynlourence@gmail.com, 'Instructor')
cursor.execute('''insert into emp values (%s, %s, %s, %s, %s,)''', new_emp)


connection.commit()
connection.close()
