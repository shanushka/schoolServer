from models.base_model import db, BaseModel, DbModel,session


class Role(BaseModel, DbModel):

    __tablename__ = 'role'

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String)


    def __str__(self):
        return {
            'role_id': self.role_id,
            'type': self.type
        }

    @classmethod
    def create(cls, request_data):
        new_role = Role(type=request_data["type"])
        session.add(new_role)
        session.commit()
