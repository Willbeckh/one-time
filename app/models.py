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
    pitches = db.relationship(
        'Pitch', backref='author', lazy='dynamic')  # one to many
    comments = db.relationship(
        'Comment', backref='author', lazy='dynamic')  # one to many
    about_me = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    votes_id = db.Column(db.Integer, db.ForeignKey('votes.id'))
    # votes = db.relationship('Vote', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}> - <Bio: {self.about_me}>'

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
    pitch_comments = db.relationship(
        'Comment', backref="pitch", lazy='dynamic')
    categories = db.Column(db.String(10))
    votes = db.relationship('Vote', backref='pitch', lazy='dynamic')

    def __repr__(self):
        return f'<Post {self.text}>'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def __repr__(self):
        '''handler method for debugging purposes.'''
        return f'<Comment: {self.comment_text}, Pitch_id: {self.pitch_id}'


# votes
class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=0)
    downvote = db.Column(db.Integer, default=0)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user = db.relationship('User', backref='votes', lazy='dynamic')

    def __repr__(self):
        if self.upvote == 1:
            vote = 'upvote'
            return f'<Vote: {vote}>'
            # return f'<Upvote: {self.upvote}>'
        else:
            vote = 'downvote'
            return f'<Downvote: {vote}>'
