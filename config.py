from os import urandom,getenv
from dotenv import load_dotenv
class Config:
    DEBUG = True
    SECRET_KEY = urandom(20)
    load_dotenv()
    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = int(getenv('MAIL_PORT'))
    MAIL_USE_TLS = bool(getenv('MAIL_USE_TLS'))
    MAIL_DEFAULT_SENDER = getenv('MAIL_DEFAULT_SENDER')
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = 'ecgmbrltxjirldrw'