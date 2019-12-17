from flask import json, request, Flask, Blueprint
import smarthome_utils as h
from services.temperature.models import Temperature

temperature = Blueprint('temperature', __name__, url_prefix='/temperature')


@temperature.route('/')
def current():
    pass

@temperature.route("/range")
def range():
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')