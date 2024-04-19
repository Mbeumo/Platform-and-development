from models.EmployeeModel import EmployeeModel
from flask import Flask, jsonify, request


app = Flask(__name__)


class EmployeeController:
    @app.route('/employees', methods=['GET'])
    def get_all_employees(self):
        employees = EmployeeModel.fetch_all_employees()
        return jsonify(employees)

    @app.route('/employees', methods=['POST'])
    def insert_employee(self):
        data = request.json
        EmployeeModel.insert_employee(data['name'], data['age'], data['dob'], data['email'], data['gender'], data['contact'], data['address'])
        return jsonify({'message': 'Employee added successfully'})

    @app.route('/employees/<int:id>', methods=['PUT'])
    def update_employee(self, id):
        data = request.json
        EmployeeModel.update_employee(id, data['name'], data['age'], data['dob'], data['email'], data['gender'], data['contact'], data['address'])
        return jsonify({'message': 'Employee updated successfully'})

    @app.route('/employees/<int:id>', methods=['DELETE'])
    def delete_employee(self,id):
        EmployeeModel.delete_employee(id)
        return jsonify({'message': 'Employee deleted successfully'})

    if __name__ == '__main__':
        app.run(debug=True, port=5000)
