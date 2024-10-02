from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData


engine = create_engine('postgresql://postgres:123456@localhost/hr')

with engine.connect() as connection:
    meta = MetaData(engine)
    emp_table = Table('emp', meta, autoload=True, autoload_with=engine)

    # Insert
    # insert_statement = emp_table.insert().values(id=1004,
    #                                              first_name='Edy',
    #                                              last_name='Park',
    #                                              email='edy@mail.com',
    #                                              position='Developer')
    # connection.execute(insert_statement)

    # select
    select_statement = emp_table.select().where(emp_table.c.first_name=='Edy')
    result = connection.execute(select_statement)
    for r in result:
        print(r)

    # update
    update_statement = emp_table.update().where(emp_table.c.first_name=='Edy').values(email='park@mail.com')
    connection.execute(update_statement)

    # delete
    delete_statement = emp_table.delete().where(emp_table.c.first_name == 'Edy')
    connection.execute(delete_statement)
