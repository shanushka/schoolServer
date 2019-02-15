from models.base_model import BaseModel

class BaseService:
    model: BaseModel = None

    @classmethod
    def fetch(cls):
        return cls.model.fetch()

    @classmethod
    def fetch_by_id(cls,id):
        return cls.model.fetch_by_id(id)

    @classmethod
    def delete(cls,id):
        return cls.model.delete(id)