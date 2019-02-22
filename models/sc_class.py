from models.base_model import BaseModel, db,DbModel,session


class SchoolClass(BaseModel,DbModel):
    __tablename__ = 'sc_class'

    class_id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    section = db.Column(db.CHAR, nullable=False)

    def __str__(self):
        return {
            'class_id': self.class_id,
            'grade': self.grade,
            'section': self.section
        }

    @classmethod
    def create(cls, requested_data):
        new_class = SchoolClass(grade=['grade'], section=requested_data['section'])
        session.add(new_class)
        session.commit()

    @classmethod
    def update(cls, _class_id, requested_data):
        update_class = SchoolClass.query.filter_by(class_id=_class_id).first()
        update_class.grade = requested_data['grade']
        update_class.section = requested_data['section']
        session.add(update_class)
        session.commit()
