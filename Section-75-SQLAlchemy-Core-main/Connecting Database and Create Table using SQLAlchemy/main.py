import sqlalchemy as sa


engine = sa.create_engine('sqlite:///hr.db')
connection = engine.connect()

meta_data = sa.MetaData()

employees = sa.Table(
    'Employees', meta_data,
    sa.Column('id, sa.Interior(), primary_key=True),
    sa.Column('name', sa.String()),
    sa.Column('position', sa.String()),
)

  meta_data.create_all(engine)
