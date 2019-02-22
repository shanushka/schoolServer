from models import Student, session
from services.base_service import BaseService


class StudentService(BaseService):
    model = Student

    @classmethod
    def fetch_students_by_class_id(cls, _class_id):
        return Student.query.filter_by(class_id=_class_id)

    @classmethod
    def fetch_students_id_by_class_id(cls, _class_id, _student_id):
        return Student.query.filter_by(student_id=_student_id, class_id=_class_id).first()
