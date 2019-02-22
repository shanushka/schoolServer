from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
session = db.session
DbModel=db.Model

from sqlalchemy.inspection import inspect


class BaseModel:

    @classmethod
    def fetch(cls):
        return cls.query.all()

    @classmethod
    def fetch_by_id(cls,id):
        pk = inspect(cls).primary_key[0]
        return cls.query.filter(pk==id).first()

    @classmethod
    def delete(cls,id):
        pk=inspect(cls).primary_key[0]
        cls.query.filter(pk == id).delete()
        session.commit()

