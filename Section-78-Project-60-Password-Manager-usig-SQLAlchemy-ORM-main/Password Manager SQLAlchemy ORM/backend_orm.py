from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import randint, shuffle, choice


Base = declarative_base()


class Passwords(Base):
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True)
    website = Column(String)
    email = Column(String)
    password = Column(String)


class PasswordManagerBE:
    def __init__(self):
        self.engine = create_engine('sqlite:///password_data.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save_data(self, website, email, password):
        password = Passwords(website=website, email=email, password=password)
        self.session.add(password)
        self.session.commit()

    def search_password(self, website):
        query = self.session.query(Passwords).filter(Passwords.website == website).first()
        return query.id, query.website, query.email, query.password

    def generate_password(self):
        password = ""
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "1234567890"
        symbols = "-+=!@#$%^&*"
        for char in range(1, randint(8, 12)):
            password += choice(letters)
        for num in range(1, randint(3, 5)):
            password += choice(nums)
        for symbol in range(1, randint(3, 5)):
            password += choice(symbols)
        password_list = list(password)
        shuffle(password_list)
        password = "".join(password_list)
        return password