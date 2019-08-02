from datetime import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Todo(db.Document):
    title = db.StringField(max_length=60)
    text = db.StringField()
    done = db.BooleanField(default=False)
    pub_date = db.DateTimeField(default=datetime.now)

    def as_dict(self):
       return {
           "id": str(self.id),
           "title": self.title,
           "text": self.text,
           "done": self.done,
           "pub_date": self.pub_date.isoformat()
        }