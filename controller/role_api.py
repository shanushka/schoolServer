import json
from flask import request, Response

from services import RoleService
from utils.common import json_response
from controller import api_blueprint as controller
from utils.validatepayload import validRoleObject, invalidObjectMessage


@controller.route('/role', methods=['GET'])
def fetch_role():
    return json_response(RoleService.fetch())


@controller.route('/role/<int:id>', methods=['GET'])
def fetch_role_by_id(id):
    return json_response(RoleService.fetch_by_id(id))


@controller.route('/role', methods=['POST'])
def create_role():
    request_data = request.get_json()
    if (validRoleObject(request_data)):
        RoleService.create(request_data)
        return Response(json.dumps(request_data), 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage), 401, mimetype='application/json')
