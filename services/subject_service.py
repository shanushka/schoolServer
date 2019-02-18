from models import Subject,session
from services.base_service import BaseService


class SubjectService(BaseService):

    model = Subject

    @classmethod
    def fetch_subject_by_class_id(cls, _class_id):
        return Subject.query.filter_by(class_id=_class_id)

    @classmethod
    def fetch_subject_id_by_class_id(cls, _class_id, _subject_id):
        return Subject.query.filter_by(subject_id=_subject_id, class_id=_class_id).first()
