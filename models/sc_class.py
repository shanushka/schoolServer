from models.base_model import BaseModel, db,DbModel


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
