from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db
from . import login_manager

@login_manager.user_loader
def load_user(id):
    '''method that keeps the id of the current authenticated user'''
    return User.query.get(int(id))


class User(UserMixin, db.Model):
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

    # @property
    # def password(self):
    #     raise AttributeError('Password not accessble!')

    # @password.setter
    def set_password(self, password):
        """ Method to create a hashed password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''Verifies if a password is hashed.'''
        return check_password_hash(self.password_hash, password)


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Post {self.text}>'
