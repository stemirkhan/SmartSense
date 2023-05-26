from flask import Blueprint
from app import login_manager


bp_auth = Blueprint('auth', __name__, template_folder='templates',  static_folder='static')
login_manager.login_view = 'auth.login'

from .routes import *
