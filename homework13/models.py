from sqlalchemy.orm import validates
from datetime import date
from app import db

class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    author = db.Column(db.String(140), nullable=True)
    message = db.Column(db.String(3000), nullable=False)

    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True)

    @validates('message')
    def validate_message(self, key, message):
        assert len(message) > 5
        return message

    def __str__(self):
        return '<Post %r>' % self.message