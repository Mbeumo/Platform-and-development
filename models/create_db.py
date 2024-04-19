import enum

from constants import PATH_TO_DB
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dba.sqlite'  # Use SQLite for this example
db = SQLAlchemy(app)


# class CreateDb:
class TaskStatus(enum.Enum):
    Male = 'M'
    Female = 'F'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.Enum(TaskStatus), default=TaskStatus.Male)
    contact = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)


# def create_table(self):
#     create_Employee_table_query = "CREATE TABLE Employee (id int primary key auto_increment,name varchar(30), age int , dob date, email varchar(20), gender enum('M','F'), contact int, address varchar(30))";
#     create_Task_table_query = "Create Table Task(id int primary key auto_increment,description varchar(1024),due_date date,id user,id_Emp int,foreign key(id_Emp) references Employee(id))"
#     conn = self.db.create_connection()
#     cur = conn.cursor()
#     cur.execute(create_Employee_table_query)
#     cur.execute(create_Task_table_query)

# create_exam_table_query = """
# CREATE TABLE exam(academic_year TEXT, session TEXT, duration INTEGER,
# id INTEGER PRIMARY KEY AUTOINCREMENT, subject INTEGER, FOREIGN KEY(subject) REFERENCES subject(id))
# """
#
# create_file_table_query = "CREATE TABLE file(path TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT, exam INTEGER, FOREIGN KEY(exam) REFERENCES exam(id))"
#
# with sqlite3.connect(PATH_TO_DB) as connection:
#     cursor = connection.cursor()
#
#     for query in [create_subject_table_query, create_exam_table_query, create_file_table_query]:
#         cursor.execute(query)
