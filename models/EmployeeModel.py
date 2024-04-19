#from base_model import Database
from create_db import Employee


class EmployeeModel:
    def __init__(self):
            pass
        #self.db = Database()


    def fetch_all_employees(self):
        employees = self.db.session.query(Employee).all()
        return employees
        # conn = self.db.create_connection()  # Create a new connection
        # cur = conn.cursor()  # Create a new cursor
        # cur.execute("SELECT * FROM employees")
        # rows = cur.fetchall()
        # conn.close()  # Close the connection
        # return rows

    def insert_employee(self, name, age, dob, email, gender, contact, address):
        new_employee = Employee(name=name, age=age, dob=dob, email=email, gender=gender, contact=contact, address=address)
        self.db.session.add(new_employee)
        self.db.session.commit()
        # conn = self.db.create_connection()  # Create a new connection
        # cur = conn.cursor()  # Create a new cursor
        # cur.execute("INSERT INTO employees (name, age, dob, email, gender, contact, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
        #             (name, age, dob, email, gender, contact, address))
        # conn.commit()  # Commit the transaction
        # conn.close()  # Close the connection

    def update_employee(self, id, name, age, dob, email, gender, contact, address):
        employee = self.db.session.query(Employee).filter(Employee.id == id).first()
        if employee:
            employee.name = name
            employee.age=age
            employee.dob=dob
            employee.email = email
            employee.gender=gender
            employee.contact=contact
            employee.address=address
            self.db.session.commit()
        # conn = self.db.create_connection()  # Create a new connection
        # cur = conn.cursor()  # Create a new cursor
        # cur.execute("UPDATE employees SET name=?, age=?, dob=?, email=?, gender=?, contact=?, address=? WHERE id=?",
        #             (name, age, dob, email, gender, contact, address, id))
        # conn.commit()  # Commit the transaction
        # conn.close()  # Close the connection

    def delete_employee(self, idi):
        employee = self.db.session.query(Employee).filter(Employee.id == idi).first()
        if employee:
            self.db.session.delete(employee)
            self.db.session.commit()
        # conn = self.db.create_connection()  # Create a new connection
        # cur = conn.cursor()  # Create a new cursor
        # cur.execute("DELETE FROM employees WHERE id=?", (id,))
        # conn.commit()  # Commit the transaction
        # conn.close()  # Close the connection
