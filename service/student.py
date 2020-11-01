from repository.database import *


class StudentService:
    def __init__(self):
        self.__student = CONNECTION.collection["student"]

    def add_student(self, student: dict):
        self.__student.add(student)
        return self.__student.find_by_id()

    def get_students(self):
        return self.__student.find_all()

    def get_student_by_id(self, _id):
        return self.__student.find_by_id(_id)

    def delete_student(self, _id: int):
        stu = self.__student.find_by_id(_id)
        self.__student.remove_by_id(_id)
        return stu
