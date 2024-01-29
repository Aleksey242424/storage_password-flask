from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class LoginForm(FlaskForm):
    username = StringField(label='username',render_kw={'placeholder':'username'},validators=[DataRequired()])
    password = PasswordField(label='password',render_kw={'placeholder':'password'},validators=[DataRequired()])
    remember_me = BooleanField(label='remember_me')
    sign_in = SubmitField(label='sigh in')

class RegisterForm(FlaskForm):
    username = StringField(label='username',render_kw={'placeholder':'username'},validators=[DataRequired(),Length(0,255)])
    password = PasswordField(label='password',render_kw={'placeholder':'password'},validators=[DataRequired(),Length(0,255)])
    repeat_password = PasswordField(label='password',render_kw={'placeholder':'password'},validators=[EqualTo('password')])
    email = EmailField(label='email',render_kw={'placeholder':'email'},validators=[DataRequired(),Length(0,255)])
    remember_me = BooleanField(label='remember_me')
    register = SubmitField(label='register')

class ResetPasswordForm(FlaskForm):
    email = EmailField(label='email',render_kw={'placeholder':'email'},validators=[DataRequired(),Email()])
    send_email = SubmitField(label='send')

class NewPasswordForm(FlaskForm):
    password = PasswordField(label='password',render_kw={'placeholder':'password'},validators=[DataRequired(),Length(0,255)])
    repeat_password = PasswordField(label='repeat_password',render_kw={'placeholder':'repeat password'},validators=[EqualTo('password')])
    update_password = SubmitField(label='update password')