from models import Users
from flask import session,jsonify
from functools import wraps
from services.users_service import UserService
from enums import RoleEnum


class Login:

    @classmethod
    def IsUserMatched(cls, requested_data):
        email = requested_data['email']
        password = requested_data["password"]

        return UserService.IsUserMatched(email,password)

    @classmethod
    def authenticate(cls, roles=None):

        def real_decorator(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                print(roles)

                if "email" in session:
                    user = Users.query.filter_by(email=session["email"]).first()

                    if(RoleEnum.get_by_id(user.role_id) in roles):
                        return func(*args, **kwargs)
                else:
                    return jsonify({'error': 'Need to login to view this page'}), 401
            return wrapper
        return real_decorator
