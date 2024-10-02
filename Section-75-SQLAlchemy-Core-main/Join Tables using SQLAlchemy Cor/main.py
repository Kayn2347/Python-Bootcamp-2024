import sqlalchemy as sa


engine = sa.create_engine('sqlite:///hr.db')
connection = engine.connect()
meta_data = sa.MetaData()

employees = sa.Table('Employees', meta_data, autoload_with=engine)
departments = sa.Table('Departments', meta_data, autoload_with=engine)

new_query = sa.select([employees, departments]).where(employees.c.Dep_ID==departments.c.Dep_ID)
result = connection.execute(new_query).fetchall()
print(result)

