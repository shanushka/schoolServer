from models import Users, session
from services.base_service import BaseService


class UserService(BaseService):
    model = Users

    @classmethod
    def create(cls, request_data):
        new_users = Users(name=request_data["name"], password=request_data["password"], email=request_data["email"],
                          contact_number=request_data["contact_number"], role_id=request_data["role_id"])
        session.add(new_users)
        session.commit()

    @classmethod
    def update(cls, user_id, request_data):
        user = Users.query.filter_by(user_id=user_id).first()
        user.name = request_data["name"]
        user.password = request_data["password"]
        user.contact_number = request_data["contact_number"],
        user.role_id = request_data["role_id"],
        user.email = request_data["email"]
        session.add(user)
        session.commit()

