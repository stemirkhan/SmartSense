from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_admin import Admin
from flask_mail import Mail
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)


from app.auth import bp_auth
app.register_blueprint(bp_auth)

from app.errors import bp_errors
app.register_blueprint(bp_errors)

from app.general import bp_general
app.register_blueprint(bp_general)

from app.models import User, RoleUser, Role, ServerAccessToken, SensorReading
from app.admin import *
admin_panel = Admin(app, name='SmartSense', template_mode='bootstrap4', index_view=HomeAdminView())
admin_panel.add_view(ModelUserView(User, db.session, name='Users'))
admin_panel.add_view(ModelRoleView(Role, db.session, name='Roles'))
admin_panel.add_view(BaseModelView(RoleUser, db.session, name='User roles'))
admin_panel.add_view(BaseModelView(ServerAccessToken, db.session, name='Server token'))
admin_panel.add_link(MainIndexLink(name='Back'))