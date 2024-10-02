from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# TODO 1 - Create Connection

class Employee():
    pass
    # TODO 2 - Employee Table


class Contact():
    pass
    # TODO 3 - Employee Table


class Database:
    def __init__(self):
        pass
        # TODO 4 - Initialize session

    # Insert Function
    def insert(self, name, age, dob, email, gender, contact, address):
        pass
        # TODO 4 - Insert into employees and details

    # Fetch Employee Data
    def fetch(self):
        result = []
        rows = self.session.query(Employee).all()
        for row in rows:
            result.append((row.id, row.name,row.age, row.dob, row.gender))
        return result

    # Fetch Details
    def fetch_details(self, emp_id):
        result = []
        # TODO 5 - IFetch Details
        return result

    # Delete a Record in DB
    def remove(self, id):
        pass
        # TODO 6 - Delete records from both tables

    # Update a Record in DB
    def update(self, id, name, age, dob, email, gender, contact, address):
        pass
        # TODO 7 - Update records in both tables






