from app.models import Pitch
from .. import main
from flask import render_template, redirect, flash, url_for
from flask_login import login_required


@main.route('/')
@main.route('/index')
@login_required
def index():
    """
    Function for rendering the root page.
    """
    pitches = Pitch.query.all()
    print(pitches)
    title = 'Pitchy'
    return render_template('index.html', title=title, pitches=pitches)
