from flask import json, request, Flask, Blueprint, current_app
from services.dust.models import Dust
import smarthome_utils as h

dust = Blueprint('dust', __name__, url_prefix='/dust')


@dust.route('/')
def current():
    latest_dust = Dust.query.order_by(Dust.enddate.desc()).first()
    latest_dust = latest_dust if latest_dust is not None else Dust()
    return h.getResponse(current_app,latest_dust.to_json())

@dust.route("/range")
def range():
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')