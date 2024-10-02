import sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship


engine = sa.create_engine('sqlite:///hr.db')
Base = declarative_base()


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)


class Projects(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employee.id'))
    name = Column(String)
    employees = relationship('Employees', back_populates='projects')


Employees.projects = relationship('Projects', back_populates='employees')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

emp1 = Employees(name='Kayn', position='Developer')
emp1.projects = [Projects(name='Python for Everyone'), Projects(name='Python DSA')]
session.add(emp1)
session.commit()


