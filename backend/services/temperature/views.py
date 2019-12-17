from flask import json, request, Flask, Blueprint, current_app
import smarthome_utils as h
from services.temperature.models import Temperature

temperature = Blueprint('temperature', __name__, url_prefix='/temperature')


@temperature.route('/')
def current():
    latest_temp = Temperature.query.order_by(Temperature.timestamp.desc()).first()
    latest_temp = latest_temp if latest_temp is not None else Temperature()
    return h.getResponse(current_app,latest_temp.to_json())

@temperature.route("/range")
def range():
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')