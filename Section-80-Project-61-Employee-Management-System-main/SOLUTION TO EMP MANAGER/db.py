from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'emp'}
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    age = Column(String(length=100))
    dob = Column(String(length=100))
    email = Column(String(length=100))
    gender = Column(String(length=100))
    contact = Column(String(length=100))
    address = Column(String(length=250))


class Database:
    def __init__(self):
        self.engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/emp")
        Base.metadata.create_all(self.engine)
        self.session_maker = sessionmaker()
        self.session_maker.configure(bind=self.engine)
        self.session = self.session_maker()

    # Insert Function
    def insert(self, name, age, dob, email, gender, contact, address):
        new_emp = Employee(name=name, age=age, dob=dob, email=email, gender=gender, contact=contact, address=address)
        self.session.add(new_emp)
        self.session.commit()

    # Fetch All Data from DB
    def fetch(self):
        results = []
        rows = self.session.query(Employee).all()
        for row in rows:
            results.append((row.id, row.name, row.age, row.dob, row.email, row.gender, row.contact, row.address))
        return results

    # Delete a Record in DB
    def remove(self, id):
        emp = self.session.query(Employee).filter(Employee.id == id).first()
        self.session.delete(emp)
        self.session.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, email, gender, contact, address):
        emp = self.session.query(Employee).filter(Employee.id == id).first()
        emp.name = name
        emp.age = age
        emp.dob = dob
        emp.email = email
        emp.gender = gender
        emp.contact = contact
        emp.address = address
        self.session.commit()






