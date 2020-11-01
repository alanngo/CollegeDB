from flask import Blueprint, request, jsonify
from service.student import StudentService

student = Blueprint("student", __name__)
student_service = StudentService()


@student.route('/students', methods=['POST'])
def add_student():
    obj = request.get_json()
    student_service.add_student(obj)


@student.route('/students', methods=['GET'])
def get_students():
    return jsonify(student_service.get_students())


@student.route('/students/<_id>', methods=['DELETE'])
def delete_student(_id):
    return student_service.delete_student(_id)
