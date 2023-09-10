from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, EqualTo


class SignUpForm(FlaskForm):
    first_name = StringField('first name', validators=[InputRequired()])
    last_name = StringField('last name', validators=[InputRequired()])
    username = StringField('username', validators=[InputRequired()])
    email = EmailField('email', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    confirm_pass = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('sign up')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('log in')
