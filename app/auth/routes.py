from flask import render_template,redirect,url_for
from app.auth import auth_bp
from flask_login import current_user
from app.system_db.users import Users

@auth_bp.route('/')
def login():
    if current_user.is_anonymous:
        return
    return