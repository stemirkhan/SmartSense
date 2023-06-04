#!/usr/bin/python

import os
from app import create_app

LEFT_USER_PSW = os.environ.get('LEFT_USER_PSW')
LEFT_USER_NAME = os.environ.get('LEFT_USER_NAME')

app = create_app(config_class='config.ProductionConfig')


with app.app_context():  
    from app.models import db, User, Role,  RoleUser
    
    role = Role(id=1, name='Admin')
    db.session.add(role)
    db.session.commit()
    
    user = User(email='admin@gmail.com', firstname=LEFT_USER_PSW, lastname=LEFT_USER_NAME, telegram_notifications=False)
    user.password = LEFT_USER_PSW
    db.session.add(user)
    db.session.commit()
    
    role_user = RoleUser(user_id = user.id, role_name=role.name)
    db.session.add(role_user)
    db.session.commit()
    