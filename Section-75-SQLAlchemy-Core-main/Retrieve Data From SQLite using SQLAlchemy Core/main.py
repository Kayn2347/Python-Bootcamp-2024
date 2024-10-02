import sqlalchemy as sa


engine = sa.create_engine('sqlite:///hr.db')
connection = engine.connect()

meta_data = sa.MetaData()

employees = sa.Table('Employees', meta_data, autoload_with=engine)
# query = sa.select([employees])
# result = connection.execute(query)
# result_set = result.fetchall()

# query1 = sa.select([employees]).where(employees.colums.position =='Software engineer')
# result1 = connection.execute(query1)
# result_set = result.fetchall()
# print(result_set)

new_query = employees.select().where(employees.c.id == 4)
result = connection.execute(new_query)
result_set = result.fetchall()
print(result_set)
