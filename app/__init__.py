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
    return app