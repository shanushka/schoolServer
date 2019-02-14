from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

from controller import (
    users_api,
    role_api,
    students_api,
    classes_api,
    subjects_api
)
