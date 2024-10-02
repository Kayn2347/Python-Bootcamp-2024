import mysql.connector as mysql
import csv


connection = mysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           database='company')
cursor = connection.cursor()

create_query = '''CREATE TABLE IF NOT EXISTS agent (
                id INT NOT NULL AUTO_INCREMENT,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                email VARCHAR(50),
                city VARCHAR(50),
                PRIMARY KEY (id))'''

cursor.execute(create_query)

with open('representative.csv', 'r') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        row_tuple = tuple(row)
        cursor.execute('''INSERT INTO agent (first_name, last_name, email, city) VALUES
                        (%s, %s, %s, %s)''', row_tuple)

connection.commit()