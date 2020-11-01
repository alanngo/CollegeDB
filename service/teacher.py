from repository.database import *

STUDENT = CONNECTION.collection["student"]


class TeacherService:
    def __init__(self):
        self.__teacher = CONNECTION.collection["teacher"]

    def add_teacher(self, firstname, lastname, teacher: dict):
        _id = f"{firstname}.{lastname}@mongocollege.edu"
        self.__teacher.add_by_id(_id, teacher)
        return self.__teacher.find_by_id(_id)

    def get_teachers(self):
        return self.__teacher.find_all()

    def updateClassroom(self, student, teacher_id, update_type):
        if update_type == "ENROLL":
            self.__teacher.update_by_id(teacher_id, key="students", value=student, aggregate=PUSH)
        elif update_type == "UNENROLL":
            teach = self.__teacher.find_by_id(teacher_id)
            stu_list = teach["students"]
            stu_list.remove(student)
            self.__teacher.update_by_id(teacher_id, key="students", value=stu_list)
        else:
            raise RuntimeError("Invalid Choice")
        return self.__teacher.find_by_id(teacher_id)
