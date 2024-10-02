from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import pandas


engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/company")

Base = declarative_base()


class Agent(Base):
    __tablename__ = 'agents'
    __table_args__ = {'schema': 'company'}
    id = Column(Integer, primary_key=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    email = Column(String(length=50))
    city = Column(String(length=50))


Base.metadata.create_all(engine)

df = pandas.read_csv('representative.csv')
df.to_sql(con=engine, name=Agent.__tablename__, if_exists='append', index=False)