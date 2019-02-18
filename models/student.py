from models.base_model import BaseModel, db,DbModel,session

class Student(BaseModel,DbModel):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.Integer)
    contact_number = db.Column(db.Integer, nullable=False)
    father_name = db.Column(db.String(100))
    mother_name = db.Column(db.String(100))
    class_id = db.Column(db.Integer, db.ForeignKey("sc_class.class_id"))

    def __str__(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'roll_number': self.roll_number,
            'contact_number': self.contact_number,
            'father_name': self.father_name,
            'mother_name': self.mother_name,
            'class_id': self.class_id
        }

    @classmethod
    def create(cls, request_data):
        new_student = Student(name=request_data["name"], father_name=request_data["father_name"],
                              mother_name=request_data["mother_name"],
                              contact_number=request_data["contact_number"], class_id=request_data["class_id"])
        session.add(new_student)
        session.commit()

    @classmethod
    def update(cls, _student_id, _requested_date):
        updated_student = Student.query.filter_by(student_id=_student_id).first()
        updated_student.name = _requested_date['name']
        updated_student.father_name = _requested_date['father_name']
        updated_student.mother_name = _requested_date['mother_name']
        updated_student.contact_number = _requested_date['contact_number']
        updated_student.class_id = _requested_date['class_id']
        session.add(updated_student)
        session.commit

