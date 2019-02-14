from models.base_model import db, BaseModel, DbModel


class Role(BaseModel, DbModel):

    __tablename__ = 'role'

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String)


    def __str__(self):
        return {
            'role_id': self.role_id,
            'type': self.type
        }
