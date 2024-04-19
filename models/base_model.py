# from abc import ABC, abstractmethod
# import json

# class AbstractBaseModel(ABC, dict):
#     def __init__(self) -> None:
#         self.id = None
#         super().__init__()
#     @abstractmethod
#     def save(self):
#         pass
#
#     @abstractmethod
#     def read(id=None):
#         pass
#
#     @abstractmethod
#     def delete(self):
#         pass
#
#     def __str__(self):
#         return f"BaseModel {self.id}"
# """ PATH_TO_DB = os.path.join(
#     os.path.dirname(__file__),
#     "Employee.db"
# ) """
import sqlite3
import constants



class Database:
        def __init__(self):

            pass

        def create_connection(self):
            try:
                conn = sqlite3.connect(constants.PATH_TO_DB)
                return conn
            except sqlite3.Error as e:
                print(e)
                return None

        # def fetch(self):
        #     conn = self.create_connection()
        #     if conn:
        #         cur = conn.cursor()
        #         cur.execute("SELECT * FROM employees")
        #         rows = cur.fetchall()
        #         conn.close()
        #         return rows
        #     else:
        #         return []
        #
        # def insert(self, name, age, doj, email, gender, contact, address):
        #     conn = self.create_connection()
        #     if conn:
        #         cur = conn.cursor()
        #         cur.execute(
        #             "INSERT INTO employees (name, age, doj, email, gender, contact, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
        #             (name, age, doj, email, gender, contact, address))
        #         conn.commit()
        #         conn.close()
        #
        # def update(self, id, name, age, doj, email, gender, contact, address):
        #     conn = self.create_connection()
        #     if conn:
        #         cur = conn.cursor()
        #         cur.execute(
        #             "UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",
        #             (name, age, doj, email, gender, contact, address, id))
        #         conn.commit()
        #         conn.close()
        #
        # def remove(self, id):
        #     conn = self.create_connection()
        #     if conn:
        #         cur = conn.cursor()
        #         cur.execute("DELETE FROM employees WHERE id=?", (id,))
        #         conn.commit()
        #         conn.close()
