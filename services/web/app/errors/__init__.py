from flask import Blueprint


bp_errors = Blueprint('errors', __name__, template_folder='templates',  static_folder='static')

from .routes import *
