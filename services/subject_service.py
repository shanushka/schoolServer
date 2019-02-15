from models import Subject,session
from services.base_service import BaseService


class SubjectService(BaseService):

    model = Subject

    @classmethod
    def fetch_by_id(cls, _subject_id):
        return Subject.query.filter_by(subject_id=_subject_id).first()

    @classmethod
    def create(cls, request_data):
        new_subject = Subject(name=request_data["name"], class_id=request_data["class_id"])
        session.add(new_subject)
        session.commit()

    @classmethod
    def delete(cls, _subject_id):
        Subject.query.filter_by(subject_id=_subject_id).delete()
        session.commit()

    @classmethod
    def update(cls, _subject_id, _requested_date):
        updated_subject = Subject.query.filter_by(subject_id=_subject_id).first()
        updated_subject.name = _requested_date['name']
        updated_subject.class_id = _requested_date['class_id']
        session.add(updated_subject)
        session.commit()

    @classmethod
    def fetch_subject_by_class_id(cls, _class_id):
        return Subject.query.filter_by(class_id=_class_id)

    @classmethod
    def fetch_subject_id_by_class_id(cls, _class_id, _subject_id):
        return Subject.query.filter_by(subject_id=_subject_id, class_id=_class_id).first()
