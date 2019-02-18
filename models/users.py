from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from models.base_model import BaseModel, db, DbModel,session


class Users(BaseModel, DbModel):
    __tablename__ = 'users'

    user_id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String)
    email = db.Column(db.String)
    contact_number = db.Column(db.BigInteger)
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"))

    def __init__(self,  name, password, email, contact_number, role_id,user_id=None):
        if user_id == None:
            user_id = uuid4()

        self.user_id = user_id
        self.name = name
        self.password = password
        self.email = email
        self.contact_number = contact_number
        self.role_id = role_id

    def __str__(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'contact_number': self.contact_number,
            'role_id': self.role_id

        }

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
