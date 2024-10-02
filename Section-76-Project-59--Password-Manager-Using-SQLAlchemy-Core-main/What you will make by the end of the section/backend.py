import sqlite3
from random import choice, randint, shuffle


class PasswordManagerBE:
    def __init__(self):
        connection = sqlite3.connect("password_data.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Passwords (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT, Website TEXT,
                        Email TEXT, Password TEXT)''')
        connection.commit()
        connection.close()

    def save_data(self, website, email, password):
        connection = sqlite3.connect("password_data.db")
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO Passwords (Website, Email, Password)
                        Values (?, ?, ?)''', (website, email, password))
        connection.commit()
        connection.close()

    def search_password(self, website):
        connection = sqlite3.connect("password_data.db")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Passwords WHERE website = ?''', (website,))
        result = cursor.fetchone()
        connection.commit()
        connection.close()
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


