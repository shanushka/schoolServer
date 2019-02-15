from models.base_model import BaseModel, db, DbModel


class Subject(BaseModel, DbModel):
    subject_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('sc_class.class_id'))

    def __str__(self):
        return {
            "subject_id": self.subject_id,
            "name": self.name,
            "class_id": self.class_id
        }
