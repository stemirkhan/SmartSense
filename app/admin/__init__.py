from flask_admin.contrib.sqla import ModelView
from wtforms.validators import Email


class ModelUserView(ModelView):
    column_hide_backrefs = False
    column_display_pk = True

    form_columns = ('email', 'password', 'firstname', 'lastname',
                    'data_register', 'telegram_login', 'telegram_notifications')

    form_args = {
        'email': {'validators': [Email()]},
    }


class ModelRoleView(ModelView):
    column_display_pk = True


class ModelRoleUserView(ModelView):
    column_display_pk = True


class ModelServerTokenView(ModelView):
    column_display_pk = True


class ModelSensorReadingView(ModelView):
    column_display_pk = True

    can_create = False
    can_delete = False
    can_edit = False
    can_export = True

    export_max_rows = 500
    export_types = ['csv']
