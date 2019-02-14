from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
session = db.session
DbModel=db.Model


class BaseModel:

    @classmethod
    def fetch(cls):
        return cls.query.all()


