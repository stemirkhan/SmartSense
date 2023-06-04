from flask import render_template, jsonify, request
from flask_login import login_required

from . import bp_general
from app.models import SensorReading, db


@bp_general.route('/dashboard')
@bp_general.route('/')
@login_required
def dashboard():
    readings_value = db.session.query(SensorReading).order_by(SensorReading.id.desc()).first()
    sensor_readings = []
    if readings_value:
        sensor_readings = [('Температура', 'temperature', readings_value.temperature),
                       ('Влажность', 'humidity', readings_value.humidity),
                       ('Угарный газ', 'carbon_monoxide', readings_value.carbon_monoxide),
                       ('Атмосферное давление', 'atmosphere_pressure', readings_value.pressure)]
    
    else:
        sensor_readings = [('Температура', 'temperature', 0),
                       ('Влажность', 'humidity', 0),
                       ('Угарный газ', 'carbon_monoxide', 0),
                       ('Атмосферное давление', 'atmosphere_pressure', 0)]
        
    
    

    if request.is_json:
        return jsonify({kit[1]: kit[2] for kit in sensor_readings})

    return render_template('general/dashboard.html', sensor_readings=sensor_readings, title='Dashboard')