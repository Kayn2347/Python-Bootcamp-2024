from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/hr")

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'hr'}
    emp_id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    position = Column(String(length=25))


    def __repr__(self):
        return f"<name:{self.name}, position:{self.position}>"


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'hr'}
    task_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('hr.employees.emp_id'))
    description = Column(String(length=50))
    emp = relationship('Employee')

    def __repr__(self):
        return f"<emp_id:{self.emp_id}, description:{self.description}>"


class Department(Base):
    __tablename__ = 'departments'
    __table_args__ = {'schema': 'hr'}
    dep_id = Column(Integer, primary_key=True)
    name = Column(String(length=20))


Base.metadata.create_all(engine)

session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()



