from crypt import methods
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user
from .. import main  # blueprint
from app import db
from app.models import User, Pitch  # db models
from app.forms import ProfileUpdate, AddPost

# TODO: create a before request to get user last seen time.


@main.route('/')
@main.route('/index')
# @login_required
def index():
    """
    Function for rendering the root page.
    """
    pitches = Pitch.query.all()
    return render_template('index.html', title='Pitchy', pitches=pitches)


# view availabe posts for specific user
@main.route('/user/<username>')
def user(username):
    """
    method to query db for a specific user
    """
    user = User.query.filter_by(username=username).first_or_404()
    pitches = Pitch.query.all()
    return render_template('user.html', user=user, pitches=pitches)


# user update route
@main.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    """method to update a user profile"""
    # create form obj
    form = ProfileUpdate()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Profile successfully updated.')
        return redirect(url_for('main.user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.username.data = current_user.username
    return render_template('edit_profile.html', title='Update', form=form)


# # user profile photo update route
# @main.route('/user/<username>/update_profile/pic', methods=['POST'])
# @login_required
# def update_pic(username):
#     user = User.query.filter_by(username=username).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.display_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.user', username=current_user))

# crete form for creating a new post
@main.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    """Method to enable a user to create a new post"""
    form =  AddPost()
    # validate form on submit
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, text=form.text.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash(f"Post: '{pitch.title}' created successfully")
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html', title="Add post", form=form)