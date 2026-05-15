from extensions import db

from flask_login import UserMixin

from itsdangerous import URLSafeTimedSerializer

from flask import current_app


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        default='user'
    )

    bio = db.Column(
        db.Text,
        default='Hello from ConnectX'
    )

    profile_pic = db.Column(
        db.String(255),
        default='default.png'
    )

    posts = db.relationship(
        'Post',
        backref='author',
        lazy=True
    )

    comments = db.relationship(
        'Comment',
        backref='user',
        lazy=True
    )

    likes = db.relationship(
        'Like',
        backref='user',
        lazy=True,
        cascade='all, delete-orphan'
    )

    # ================= RESET TOKEN =================

    def get_reset_token(self):

        serializer = URLSafeTimedSerializer(
            current_app.config['SECRET_KEY']
        )

        return serializer.dumps(
            self.email,
            salt='password-reset-salt'
        )

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):

        serializer = URLSafeTimedSerializer(
            current_app.config['SECRET_KEY']
        )

        try:

            email = serializer.loads(
                token,
                salt='password-reset-salt',
                max_age=expires_sec
            )

        except:

            return None

        return User.query.filter_by(
            email=email
        ).first()

    def __repr__(self):

        return f"User('{self.username}')"