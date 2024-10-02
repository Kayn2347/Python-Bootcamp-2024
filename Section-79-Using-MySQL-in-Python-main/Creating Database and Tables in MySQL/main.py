-- create database hr;

use hr;

create table employees (emp_id int not null auto_increment,

                        name varchar(20),
                           position varchar(25),
                           primary key (emp_id));

create table task (task_id int not null auto_increment,
                   emp_id int,
                   description varchar(255),
                   primary key (task_id),
                   foreign key (emp_id) Reference employee(emp_id))

insert into employees(name, position) values ('Kayn', 'Developer');
insert into employees(name, position) values ('Dhea', 'Software Specialist');

SELECT 'employees'.'emp_id',
     'employees'.'name',
     'employees'.'position'
FROM 'hr'.'employees';

SELECT 'task'.'task_id'.
     'tasks'. 'emp_id',
     'tasks'. 'description'
FROM 'hr'.'task';
