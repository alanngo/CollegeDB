from flask import Blueprint, request, jsonify
from service.teacher import TeacherService
teacher = Blueprint("teacher", __name__)
teacherService = TeacherService()


@teacher.route('/teachers/<first>/<last>', methods=['POST'])
def add_teacher(first, last):
    return teacherService.add_teacher(firstname=first,
                                      lastname=last,
                                      teacher=request.get_json())


@teacher.route('/teachers', methods=['GET'])
def get_teachers():
    return jsonify(teacherService.get_teachers())
