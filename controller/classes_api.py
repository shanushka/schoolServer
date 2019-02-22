import json
from flask import request, Response

from services import ClassService
from utils.common import json_response
from controller import api_blueprint as controller
from utils.validatepayload import validClassObject, invalidObjectMessage


@controller.route('/class', methods=['GET'])
def fetch_class():
    return json_response(ClassService.fetch())


@controller.route('/class/<string:class_id>', methods=['GET'])
def fetch_class_by_id(class_id):
    return json_response(ClassService.fetch_by_id(class_id))


@controller.route('/class', methods=['POST'])
def create_class():
    request_data = request.get_json()

    if (validClassObject(request_data)):
        ClassService.create(request_data)
        return Response(json.dumps(request_data), 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage))


@controller.route('/class/<string:class_id>', methods=['PUT'])
def update_class(class_id):
    request_data = request.get_json()

    if (validClassObject(request_data)):
        ClassService.update(class_id, request_data)
        return Response(json.dumps(request_data), 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage))


@controller.route('/class/<string:class_id>', methods=['DELETE'])
def delete_class(class_id):
    if (ClassService.delete(class_id)):
        ClassService.delete(class_id)
        return Response('', 200, mimetype='application/json')
    else:
        return Response('Unable to perform delete operation', 406, mimetype='application/json')

