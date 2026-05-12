from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    email = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(255))


class Prompt(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.Text)


class JournalEntry(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255))

    content = db.Column(db.Text)

    mood = db.Column(db.String(50))

    image = db.Column(db.String(255))

    audio = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )