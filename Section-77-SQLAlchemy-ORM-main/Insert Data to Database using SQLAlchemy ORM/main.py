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
# row1 = Employees(name='Kayn', position='Developer')
# session.add(row1)
session.add_all([Employees(name='Kayn', position='Software Specialist'),
                 Employees(name='Dhea', position='Software Specialist'),
                 Employees(name='John', position='Software Engineer')])



session.commit()
    
