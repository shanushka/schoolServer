import json
from flask import request, Response

from services import SubjectService
from utils.common import json_response
from controller import api_blueprint as controller
from utils.test import validSubjectObject, invalidObjectMessage


@controller.route('/subject', methods=['GET'])
def fetch_subject():
    return json_response(SubjectService.fetch())

@controller.route('/subject/<int:subject_id>', methods=['GET'])
def fetch_subject_by_id(subject_id):
    return json_response(SubjectService.fetch_by_id(subject_id))


@controller.route('/subject', methods=['POST'])
def create_subject():
    request_data = request.get_json()
    if (validSubjectObject(request_data)):
        SubjectService.create(request_data)
        return Response('', 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage), 401, mimetype='application/json')


@controller.route('/subject/<int:subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    SubjectService.delete(subject_id)
    return Response('', 200, mimetype='application/json')


@controller.route('/subject/<int:subject_id>', methods=['PUT'])
def update_subject(subject_id):
    request_data = request.get_json()
    if (validSubjectObject(request_data)):
        SubjectService.update(subject_id,request_data)
        return Response('', 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage), 401, mimetype='application/json')

@controller.route('/class/<int:class_id>/subject', methods=['GET'])
def fetch_subject_by_class_id(class_id):
    return json_response(SubjectService.fetch_subject_by_class_id(class_id))

@controller.route('/class/<int:class_id>/subject/<int:subject_id>', methods=['GET'])
def fetch_subject_id_by_class_id(class_id,subject_id):
    return json_response(SubjectService.fetch_subject_id_by_class_id(class_id,subject_id))




