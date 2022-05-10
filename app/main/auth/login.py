'''login route'''
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from app.models import User
from . import auth
from app.forms import LoginForm

# login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function that creates the login logic.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password.")
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)



@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))