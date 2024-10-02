import mysql.connector as mysql


def connect(db_name):
    try:
        return mysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database=db_name)
    except Exception as e:
        print(e)


def add_new_employee(cursor, name, position, task_descriptions):
    new_emp = (name, position)
    cursor.execute('''insert into employees(name, position) values (%s, %s)''', new_emp)
    emp_id = cursor.lastrowid
    tasks = []
    for task in task_descriptions:
        task_data = (emp_id, task)
        tasks.append(task_data)
    cursor.executemany('''insert into tasks(emp_id, description) values (%s, %s)''', tasks)


db = connect('hr')
cursor = db.cursor()
tasks = ['Development', 'Documentation', 'Unit Testing']
add_new_employee(cursor, 'John', 'Developer', tasks)

# cursor.execute('select * from employees')
# emp_record = cursor.fetchall()
# print(emp_record)

db.commit()
db.close()
