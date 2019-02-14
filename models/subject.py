from models.base_model import BaseModel,db

class Subject(BaseModel):

    subject_id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(100),nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey('sc_class.class_id'))