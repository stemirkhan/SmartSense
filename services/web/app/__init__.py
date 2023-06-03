from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from flask_migrate import Migrate


db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
migrate = Migrate()
admin_panel = Admin()


def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # adding blueprints
    from app.auth import bp_auth
    app.register_blueprint(bp_auth)

    from app.errors import bp_errors
    app.register_blueprint(bp_errors)

    from app.general import bp_general
    app.register_blueprint(bp_general)

    # initializing the settings and adding the admin panel
    from app.admin import initialize_settings
    initialize_settings(admin_panel)
    admin_panel.init_app(app)

    return app
