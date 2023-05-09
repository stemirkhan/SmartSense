from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

from app.models import User, RoleUser, Role, ServerAccessToken, SensorReading
from app.admin import *
admin_panel = Admin(app, name='SmartSense', template_mode='bootstrap4')
admin_panel.add_view(ModelUserView(User, db.session))
admin_panel.add_view(ModelRoleView(Role, db.session))
admin_panel.add_view(ModelRoleUserView(RoleUser, db.session))
admin_panel.add_view(ModelServerTokenView(ServerAccessToken, db.session))
admin_panel.add_view(ModelSensorReadingView(SensorReading, db.session))

from . import views
