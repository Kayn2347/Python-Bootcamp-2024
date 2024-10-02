from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/hr", echo=True)

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'hr'}
    emp_id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    position = Column(String(length=25))


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'hr'}
    task_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('hr.employees.emp_id'))
    description = Column(String(length=50))
    emp = relationship('Employee')


class Department(Base):
    __tablename__ = 'departments'
    __table_args__ = {'schema': 'hr'}
    dep_id = Column(Integer, primary_key=True)
    name = Column(String(length=20))


Base.metadata.create_all(engine)
