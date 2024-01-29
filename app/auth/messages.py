from flask_mail import Message
from app import mail
from flask import render_template

def send_jwt(email,token):
    msg = Message(subject='reset your password',recipients=[email])
    msg.html = render_template('auth/reset_password_mail.html',token=token)
    mail.send(msg)