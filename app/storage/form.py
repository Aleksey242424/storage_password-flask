from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class PasswordForm(FlaskForm):
    title = StringField(label='title',render_kw={'placeholder':'title'},validators=[DataRequired(),Length(0,255)])
    password = StringField(label='password',render_kw={'placeholder':'password'},validators=[DataRequired(),Length(0,255)])
    add = SubmitField(label='Add')

class DataPasswordForm(FlaskForm):
    title = StringField(label='title',render_kw={'placeholder':'title'},validators=[DataRequired()])
    password = StringField(label='password',render_kw={'placeholder':'password'},validators=[DataRequired()])
    change = SubmitField(label='change')