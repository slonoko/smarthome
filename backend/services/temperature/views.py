from flask import json, request, Flask, Blueprint, current_app
import smarthome_utils as h
from services.temperature.models import Temperature
import datetime
from sqlalchemy import *
temperature = Blueprint('temperature', __name__, url_prefix='/temperature')

'''
if i want to use millies
from ms  to datetime --> datetime.datetime.fromtimestamp(ms/1000.0)
from datetime to ms --> dt_obj.timestamp() * 1000

url example: http://smarthome:5000/dust/range?from_date=16.12.2019-12:00&to_date=18.12.2019-17:00
'''

def toDate(dateString): 
    return datetime.datetime.strptime(dateString, "%d.%m.%Y-%H:%M").date()

@temperature.route('/', methods=['GET'])
def current():
    latest_temp = Temperature.query.order_by(Temperature.timestamp.desc()).first()
    latest_temp = latest_temp if latest_temp is not None else Temperature()
    return h.getResponse(current_app,latest_temp.__json__())

@temperature.route("/range", methods=['GET'])
def range():
    from_date = request.args.get('from_date', default = datetime.date.today(), type = toDate)
    to_date = request.args.get('to_date', default = datetime.date.today(), type = toDate)
    list_temps = Temperature.query.filter(Temperature.timestamp.between(from_date,  to_date)).order_by(Temperature.timestamp.desc()).all()
    result = [o.__json__() for o in list_temps]
    return h.getResponse(current_app,result)