from flask import Blueprint

storage_bp = Blueprint('storage_bp',__name__,template_folder='templates')

from app.storage import routes