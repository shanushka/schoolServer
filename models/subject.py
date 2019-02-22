from models.base_model import BaseModel, db, DbModel,session


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

    @classmethod
    def create(cls, request_data):
        new_subject = Subject(name=request_data["name"], class_id=request_data["class_id"])
        session.add(new_subject)
        session.commit()

    @classmethod
    def update(cls, _subject_id, _requested_date):
        updated_subject = Subject.query.filter_by(subject_id=_subject_id).first()
        updated_subject.name = _requested_date['name']
        updated_subject.class_id = _requested_date['class_id']
        session.add(updated_subject)
        session.commit()