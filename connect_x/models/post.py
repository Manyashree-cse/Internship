# from app import db
from extensions import db
from datetime import datetime

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(db.Text, nullable=False)

    image = db.Column(db.String(255),nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all,delete')

    likes = db.relationship(
    'Like',
    backref='post',
    lazy=True,
    cascade='all, delete-orphan'
)

    def __repr__(self):
        return f"Post('{self.id}')"