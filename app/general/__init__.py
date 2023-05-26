from flask import Blueprint


bp_general = Blueprint('general', __name__, template_folder='templates',  static_folder='static')

from .routes import *
