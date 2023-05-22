from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)

from app.models import User, RoleUser, Role, ServerAccessToken, SensorReading
from app.admin import *
admin_panel = Admin(app, name='SmartSense', template_mode='bootstrap4', index_view=HomeAdminView())
admin_panel.add_view(ModelUserView(User, db.session, name='Users'))
admin_panel.add_view(ModelRoleView(Role, db.session, name='Roles'))
admin_panel.add_view(BaseModelView(RoleUser, db.session, name='User roles'))
admin_panel.add_view(BaseModelView(ServerAccessToken, db.session, name='Server token'))
admin_panel.add_link(MainIndexLink(name='Back'))

from . import views
