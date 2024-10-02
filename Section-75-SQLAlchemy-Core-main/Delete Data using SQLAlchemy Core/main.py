import sqlalchemy as sa


engine = sa.create_engine('sqlite:///hr.db')
connection = engine.connect()

meta_data = sa.MetaData()

employees = sa.Table(
    'Employees', meta_data,
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('name', sa.String()),
    sa.Column('position', sa.String()),
)

meta_data.create_all(engine)

employee_list = [
    {'name':'Renad', 'position':'Software developer'},
    {'name':'Edy', 'position':'Software engineer'},
    {'name':'John', 'position':'Software specialist'},
]

# query = employees.insert().values(name='Renad', position='Software engineer')
result = connection.execute(employees.insert(), employee_list)
# print(result.inserted_primary_key)
