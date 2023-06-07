#!/usr/bin/python

import os
from app import create_app

LEFT_USER_PSW = os.environ.get('LEFT_USER_PSW')
LEFT_USER_EMAIL = os.environ.get('LEFT_USER_EMAIL')

app = create_app(config_class='config.ProductionConfig')


with app.app_context():  
    from app.models import db, User, Role,  RoleUser
    
    role = Role(id=1, name='Admin')
    db.session.add(role)
    db.session.commit()
    
    user = User(email=LEFT_USER_EMAIL, firstname='admin', lastname='admin', telegram_notifications=False)
    user.password = LEFT_USER_PSW
    db.session.add(user)
    db.session.commit()
    
    role_user = RoleUser(user_id = user.id, role_name=role.name)
    db.session.add(role_user)
    db.session.commit()
    