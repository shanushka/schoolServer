from models import Student,session
from services.base_service import BaseService


class StudentService(BaseService):
    model = Student

    @classmethod
    def fetch_by_id(cls,_student_id):
        return Student.query.filter_by(student_id = _student_id).first()

    @classmethod
    def create(cls,request_data):
        new_student = Student(name=request_data["name"], father_name=request_data["father_name"], mother_name=request_data["mother_name"],
                          contact_number=request_data["contact_number"], class_id=request_data["class_id"])
        session.add(new_student)
        session.commit()


    @classmethod
    def delete(cls,_student_id):
        Student.query.filter_by(student_id=_student_id).delete()

    @classmethod
    def update(cls,_student_id,_requested_date):
        updated_student=Student.query.filter_by(student_id=_student_id).first()
        updated_student.name = _requested_date['name']
        updated_student.father_name =  _requested_date['father_name']
        updated_student.mother_name = _requested_date['mother_name']
        updated_student.contact_number = _requested_date['contact_number']
        updated_student.class_id =_requested_date['class_id']
        session.add(updated_student)
        session.commit