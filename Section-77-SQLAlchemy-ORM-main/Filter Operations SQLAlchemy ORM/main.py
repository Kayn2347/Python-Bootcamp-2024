import sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = sa.create_engine('sqlite:///hr.db')
Base = declarative_base()


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


query = session.query(Employees).filter(or_(Employees.id>1, Employees.name.like('R%')))

for employee in query:
    print('Name:', employee.name, 'Position:', employee.position)

    
