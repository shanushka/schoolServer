import json
from flask import request, Response

from services import Login
from services import UserService
from enums import RoleEnum
from utils.common import json_response
from controller import api_blueprint as controller
from utils.test import validUserObject, invalidObjectMessage

@controller.route('/users', methods=['GET'])
@Login.authenticate(roles=[RoleEnum.ADMIN,RoleEnum.HR])
def fetch_users():
    return json_response(UserService.fetch())

@controller.route('/users/<string:user_id>', methods=['GET'])
@Login.authenticate(roles=[RoleEnum.ADMIN,RoleEnum.HR])
def fetch_users_by_id(user_id):
    return json_response(UserService.fetch_by_id(user_id))

@controller.route('/users', methods=['POST'])
@Login.authenticate(roles=[RoleEnum.ADMIN])
def create_users():
    request_data = request.get_json()

    if (validUserObject(request_data)):
        UserService.create(request_data)
        return Response('', 200, mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage))

@controller.route('/users/<string:user_id>',methods=['PUT'])
@Login.authenticate(roles=[RoleEnum.ADMIN])
def update_users(user_id):
    request_data = request.get_json()

    if(validUserObject(request_data)):
        UserService.update(user_id,request_data)
        return Response('',200,mimetype='application/json')
    else:
        return Response(json.dumps(invalidObjectMessage))

@controller.route('/users/<string:user_id>',methods=['DELETE'])
@Login.authenticate(roles=[RoleEnum.ADMIN])
def delete_users(user_id):
    if(UserService.delete(user_id)):
        UserService.delete(user_id)
        return Response('deleted', 200, mimetype='application/json')
    else:
        return Response('Unable to perform delete operation',401,mimetype='application/json')
