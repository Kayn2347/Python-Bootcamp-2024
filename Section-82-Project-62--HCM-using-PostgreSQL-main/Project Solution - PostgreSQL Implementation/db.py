from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:123456@localhost/emp')
Base = declarative_base(engine)
Base.metadata.reflect(engine)


class Employee(Base):
    __table__ = Base.metadata.tables['employees']


class Contact(Base):
    __table__ = Base.metadata.tables['contact_details']


class Database:
    def __init__(self):
        self.session_maker = sessionmaker()
        self.session_maker.configure(bind=engine)
        self.session = self.session_maker()

    # Insert Function
    def insert(self, name, age, dob, email, gender, contact, address):
        new_emp = Employee(name=name, age=age, dob=dob, email=email, gender=gender, contact=contact, address=address)
        self.session.add(new_emp)
        self.session.commit()
        new_contact = Contact(emp_id=new_emp.id, email=email, contact=contact, address=address)
        self.session.add(new_contact)
        self.session.commit()

    # Fetch All Data from DB
    def fetch(self):
        result = []
        rows = self.session.query(Employee).all()
        for row in rows:
            result.append((row.id, row.name, row.age, row.dob, row.gender))
        return result

    # Fetch Details
    def fetch_details(self, emp_id):
        result = []
        rows = self.session.query(Contact).filter(Contact.emp_id == emp_id).all()
        for row in rows:
            result.append((row.email, row.contact, row.address))
        return result

    # Delete a Record in DB
    def remove(self, id):
        contact = self.session.query(Contact).filter(Contact.emp_id == id).first()
        self.session.delete(contact)
        self.session.commit()
        emp = self.session.query(Employee).filter(Employee.id == id).first()
        self.session.delete(emp)
        self.session.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, email, gender, contact, address):
        emp = self.session.query(Employee).filter(Employee.id == id).one()
        contact_d = self.session.query(Contact).filter(Contact.emp_id == id).one()
        emp.name = name
        emp.age = age
        emp.dob = dob
        contact_d.email = email
        emp.gender = gender
        contact_d.contact = contact
        contact_d.address = address
        self.session.commit()






