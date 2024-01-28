from flask import Blueprint

storage_bp = Blueprint('storage',__name__,template_folder='templates')

from app.storage import routes