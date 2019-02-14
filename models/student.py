from models.base_model import BaseModel, db,DbModel


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
