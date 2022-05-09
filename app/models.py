from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), )
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    password_hash = db.Column(db.String(128))
    pitches = db.relationship('Pitch', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(255))

    def __repr__(self):
        return f'<User {self.email}> - <Bio: {self.about_me}>'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Post {self.text}>'
