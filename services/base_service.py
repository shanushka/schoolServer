from models.base_model import BaseModel

class BaseService:
    model: BaseModel = None

    @classmethod
    def fetch(cls):
        return cls.model.fetch()

