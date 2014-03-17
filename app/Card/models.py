import datetime
from app import db

class Player(db.DynamicDocument):
    # date = db.DateTimeField(default=datetime.datetime.now, required=True)
    # body = db.StringField(max_length=255, required=True)

    meta = {
        'ordering': ['-date']
    }