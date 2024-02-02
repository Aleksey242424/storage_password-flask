from flask import Flask
from flask_moment import Moment
from flask_login import LoginManager
from flask_mail import Mail
from config import Config


login = LoginManager()
mail = Mail()
moment = Moment()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    login.init_app(app)
    login.login_view = 'auth_bp.login'
    login.login_message = 'Для начала авторизуйтесь'
    mail.init_app(app)
    moment.init_app(app)
    from app.auth import auth_bp
    from app.storage import storage_bp
    app.register_blueprint(auth_bp,url_prefix='/auth/')
    app.register_blueprint(storage_bp,url_prefix='/')
    return app