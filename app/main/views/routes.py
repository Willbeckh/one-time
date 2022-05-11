from app.models import Pitch
from .. import main
from flask import render_template, redirect, flash, url_for
from flask_login import login_required
from app.models import User, Pitch


@main.route('/')
@main.route('/index')
# @login_required
def index():
    """
    Function for rendering the root page.
    """
    pitches = Pitch.query.all()
    title = 'Pitchy'
    return render_template('index.html', title=title, pitches=pitches)


# view availabe posts for specific user
@main.route('/user/<username>')
def user(username):
    """
    method to query db for a specific user
    """
    user = User.query.filter_by(username=username).first_or_404()
    pitches = Pitch.query.all()
    return render_template('user.html', user=user, pitches=pitches)
