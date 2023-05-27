from app.models import User, RoleUser, Role, ServerAccessToken, db
from flask_admin import Admin

from .views import *


def initialize_settings(admin_panel: Admin):
    admin_panel.name = 'SmartSense'
    admin_panel.template_mode = 'bootstrap4'
    admin_panel.index_view = HomeAdminView()

    admin_panel.add_view(ModelUserView(User, db.session, name='Users'))
    admin_panel.add_view(ModelRoleView(Role, db.session, name='Roles'))
    admin_panel.add_view(BaseModelView(RoleUser, db.session, name='User roles'))
    admin_panel.add_view(BaseModelView(ServerAccessToken, db.session, name='Server token'))
    admin_panel.add_link(MainIndexLink(name='Back'))
