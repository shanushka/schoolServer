from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from models.base_model import BaseModel, db, DbModel


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
