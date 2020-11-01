from flask import *
from flask_cors import *
from api.student import student, student_service
from api.teacher import teacher, teacherService
from util.error_advice import advice

app = Flask(__name__)

# routes and error handle routes
app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(advice)


@app.route('/enroll/<student_id>/<teacher_id>', methods=["PUT"])
def enroll(student_id, teacher_id):
    return teacherService.updateClassroom(student_service.get_student_by_id(student_id),
                                          teacher_id,
                                          "ENROLL")


@app.route('/unenroll/<student_id>/<teacher_id>', methods=["PUT"])
def unenroll(student_id, teacher_id):
    return teacherService.updateClassroom(student_service.get_student_by_id(student_id),
                                          teacher_id,
                                          "UNENROLL")


if __name__ == '__main__':
    CORS(app)  # lets other programs consume app
    app.debug = True
    app.run()
