import flask_sqlalchemy
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()

    def as_dict(self):
       return {
           "id": self.id,
           "title": self.title,
           "text": self.text,
           "done": self.done,
           "pub_date": self.pub_date.isoformat()
        }