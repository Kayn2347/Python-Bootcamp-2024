import sqlalchemy as sa
from random import choice, randint, shuffle


class PasswordManagerBE:
    def __init__(self):
        self.engine = sa.create_engine('sqlite:///password_data.db')
        self.connection = self.engine.connect()
        self.meta_data = sa.MetaData()
        self.passwords = sa.Table('Passwords', self.meta_data,
                                  sa.Column('Id', sa.Integer(), primary_key=True),
                                  sa.Column('Website', sa.String()),
                                  sa.Column('Email', sa.String()),
                                  sa.Column('Password', sa.String()),
                                  )
        self.meta_data.create_all(self.engine)

    def save_data(self, website, email, password):
        insert_query = self.passwords.insert().values(Website=website, Email=email, Password=password)
        self.connection.execute(insert_query)

    def search_password(self, website):
        select_query = sa.select([self.passwords]).where(self.passwords.c.Website==website)
        result = self.connection.execute(select_query).fetchone()
        return result

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


