import psycopg


connection = pyscopg.connect(dbname='hr',
                             user='postgres'
                             password='123456',
                             host='localhost'
                             port='5432')

connection.autocommit = True
cursor = connection.cursor()
cursor.execute('''call create_emp(%s, %s, %s, %s, %s,)''', (1006, 'kayn', 'lourence' , 'kaynlourence', 'Developer')
connection.close()
