'''login route'''
from flask import render_template, redirect, url_for, flash
from . import auth
from app.forms import LoginForm


# login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function that creates the login logic.
    '''
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login request for user {form.username.data}, remember={form.remember_me.data}")
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)
