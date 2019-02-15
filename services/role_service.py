from models import Role, session
from services.base_service import BaseService


class RoleService(BaseService):
    model = Role

    @classmethod
    def create(cls, request_data):
        new_role = Role(type=request_data["type"])
        session.add(new_role)
        session.commit()
