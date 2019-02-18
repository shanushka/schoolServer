from models import Users, session
from services.base_service import BaseService


class UserService(BaseService):
    model = Users




    @classmethod
    def IsUserMatched(cls,email,password):
        user = Users.query.filter_by(email=email).filter_by(password=password).first()
        if user is None:
            return False
        return True




