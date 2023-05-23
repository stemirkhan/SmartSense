from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
import jwt

from app import db, login_manager, app

from datetime import datetime
from time import time


class RoleUser(db.Model):
    __tablename__ = 'roles_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_name = db.Column(db.String(100), db .ForeignKey('roles.name'), nullable=False)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True, primary_key=True)

    users = db.relationship('RoleUser', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.name}'


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    _password_hash = db.Column(db.String(500), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    data_register = db.Column(db.DateTime, default=datetime.utcnow)
    telegram_login = db.Column(db.String(30), unique=True, nullable=True)
    telegram_notifications = db.Column(db.Boolean)

    roles = db.relationship('RoleUser', backref='role', lazy=True, cascade='all, delete-orphan')

    def has_roles(self, *args):
        return set(args).issubset({role.role_name for role in self.roles})

    def get_reset_password_token(self, expires_in=300):
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},
                          app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            check_id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except (jwt.exceptions.DecodeError, jwt.exceptions.ExpiredSignatureError):
            return False
        return User.query.get(check_id)

    def get_id(self):
        return self.id

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class ServerAccessToken(db.Model):
    __tablename__ = 'server_access_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    access_token = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return f"{self.name})"


class SensorReading(db.Model):
    __tablename__ = 'sensor_readings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    carbon_monoxide = db.Column(db.Integer)
    humidity = db.Column(db.Float)

    def __repr__(self):
        return f'SensorReading(recording_id={self.id})'


class ResetPasswordToken(db.Model):
    __tablename__ = 'reset_password_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jwt_token = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("reset_password_url", uselist=False))


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
