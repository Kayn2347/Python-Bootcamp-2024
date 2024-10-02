import sqlalchemy as sa


engine = sa.create_engine('sqlite:///hr.db')
connection = engine.connect()

meta_data = sa.MetaData()

employees = sa.Table('Employees', meta_data, autoload_with=engine)


delete_query = employees.delete().where(employees.c.id.==1)
connection.execute(delete_query)
# new_query = employees.select()
# result = connection.execute(new_query).fetchall()
# print(result)



