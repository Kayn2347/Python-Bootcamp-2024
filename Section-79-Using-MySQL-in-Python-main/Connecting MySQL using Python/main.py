import mysql.connector as mysql


def connect(db_name):
    try:
        return mysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database=db_name)
    expect Exception as e:
        print(e)


db = connect('hr')
cursor = db.cursor()
cursor.excute('select * from employees')
emp_record = cursor.fetchall()
print(emp_record)
db.close()
