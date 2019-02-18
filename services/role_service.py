from models import Role, session
from services.base_service import BaseService


class RoleService(BaseService):
    model = Role

