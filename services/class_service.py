from models import SchoolClass,session
from services.base_service import BaseService

class ClassService(BaseService):

    model = SchoolClass

    @classmethod
    def fetch_by_id(cls,_class_id):
        return SchoolClass.query.filter_by(class_id=_class_id).first()

    @classmethod
    def create(cls,requested_data):
        new_class = SchoolClass(grade=requested_data['grade'],section=requested_data['section'])
        session.add(new_class)
        session.commit()

    @classmethod
    def update(cls,_class_id,requested_data):
        update_class = SchoolClass.query.filter_by(class_id=_class_id).first()
        update_class.grade=requested_data['grade']
        update_class.section =requested_data['section']
        session.add(update_class)
        session.commit()

    @classmethod
    def delete(cls,_class_id):
        SchoolClass.query.filter_by(class_id=_class_id).delete()
        session.commit()
