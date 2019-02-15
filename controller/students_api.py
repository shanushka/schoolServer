import json
from flask import request, Response

from services import StudentService
from utils.common import json_response
from utils.test import validStudentObject, invalidObjectMessage
from controller import api_blueprint as controller


@controller.route('/student', methods=['GET'])
def fetch_student():
    return json_response(StudentService.fetch())


@controller.route('/student/<int:student_id>', methods=['GET'])
def fetch_student_by_id(student_id):
    return json_response(StudentService.fetch_by_id(student_id))


@controller.route('/student', methods=['POST'])
def create_student():
    request_data = request.get_json()
    if (validStudentObject(request_data)):
        StudentService.create(request_data)
        return Response('', 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage), 401, mimetype='application/json')


@controller.route('/student/<int:student_id>', methods=['DELETE'])
def delete(student_id):
    StudentService.delete(student_id)
    return Response('', 200, mimetype='application/json')


@controller.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    request_data = request.get_json()
    if (validStudentObject(request_data)):
        StudentService.update(student_id,request_data)
        return Response('', 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage), 401, mimetype='application/json')

@controller.route('/class/<int:class_id>/student', methods=['GET'])
def fetch_students_by_class_id(class_id):
    return json_response(StudentService.fetch_students_by_class_id(class_id))

@controller.route('/class/<int:class_id>/student/<int:student_id>', methods=['GET'])
def fetch_students_id_by_class_id(class_id,student_id):
    return json_response(StudentService.fetch_students_id_by_class_id(class_id,student_id))


