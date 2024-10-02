from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker\
from sqlalchemy.ext.declarative import declarative_base


engine =  create_engine('posgresql://postgres:123456@localhost/hr')
Base = declarative_base(engine)
Base.metadata.reflect(engine)


class Emp(Base):
    __table__ = Base.metadata.tablesp['emp']

    def __repr__(self):
        return f'<id:P{self.id}, name: {self.first_name} {self.last_name}>'


Session = sessionmaker()
session = Session()

#Select
last_emps = session.query(Emp).order_by(desc(Emp.id)).limit(10).all()
print(last_emps)

#Insert
# new_emp = Emp(id=1003, first_name= 'Jhon', last_name='Park', email='johnp@gmail.com', position='Developer)'
# session.add(new_emp)
# session.commit()

Update
update_emp = session.query(Emp).filter(Emp.id == 1003).first()
update_emp.email = 'kaynlourence1210@gmail.com'
session.commit()

#Delete
delete_emp = session.query(Emp).filter(Emp.id ==1003).first()
session.delete(delete_emp)
session.commit()
