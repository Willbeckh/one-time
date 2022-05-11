from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from wtforms.validators import Email, EqualTo
from .models import User


class LoginForm(FlaskForm):
    """
    Class that defines the login form logic
    """
    username = StringField('Username', validators=[DataRequired()])
    # email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    """
    Class that defines the Signup form.
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            return ValidationError("This username is taken!")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            return ValidationError("there is an account with that Email!")


class ProfileUpdate(FlaskForm):
    """class for creating a wtf form for updating user profile"""
    username = StringField('Username', validators=[DataRequired()])
    about_me = StringField('Bio', validators=[Length(min=2, max=200)])
    submit = SubmitField('Update')