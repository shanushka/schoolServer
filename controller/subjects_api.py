import json
from flask import request, Response

from services import SubjectService
from utils.common import json_response
from controller import api_blueprint as controller
from utils.test import validRoleObject, invalidObjectMessage


@controller.route('/subject', methods=['GET'])
def fetch_subject():
    return json_response(SubjectService.fetch())
