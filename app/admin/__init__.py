from flask_admin.contrib.sqla import ModelView
from wtforms.validators import Email
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for
from flask_admin.menu import MenuLink


class MainIndexLink(MenuLink):
    def get_url(self):
        return url_for("general.dashboard")


class BaseModelView(ModelView):
    column_hide_backrefs = False
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_roles('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/404.html')


class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_roles('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/404.html')

    def is_visible(self):
        return False


class ModelUserView(BaseModelView):
    form_columns = ('email', 'password', 'firstname', 'lastname',
                    'data_register', 'telegram_login', 'telegram_notifications')

    form_args = {
        'email': {'validators': [Email()]},
    }


class ModelRoleView(BaseModelView):

    form_columns = ('name',)
