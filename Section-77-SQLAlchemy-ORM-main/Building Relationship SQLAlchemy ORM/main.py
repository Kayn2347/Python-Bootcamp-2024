from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy import or_


engine = create_engine('sqlite:///hr.db')
Base = declarative_base()


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Employees).get(1)
session.delete(query)

session.commit()


