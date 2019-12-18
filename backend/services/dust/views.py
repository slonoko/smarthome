from flask import json, request, Flask, Blueprint, current_app
from services.dust.models import Dust
import smarthome_utils as h
import datetime

dust = Blueprint('dust', __name__, url_prefix='/dust')

@dust.route('/', methods=['GET'])
def current():
    latest_dust = Dust.query.order_by(Dust.enddate.desc()).first()
    latest_dust = latest_dust if latest_dust is not None else Dust()
    return h.getResponse(current_app,latest_dust.__json__())

@dust.route("/range", methods=['GET'])
def range():
    from_date = request.args.get('from_date', default = datetime.date.today(), type = h.to_date)
    to_date = request.args.get('to_date', default = datetime.date.today(), type =  h.to_date)
    list_dusts = Dust.query.filter(Dust.startdate.between(from_date,  to_date)).order_by(Dust.startdate.desc()).all()
    result = [o.__json__() for o in list_dusts]

    return h.getResponse(current_app,result)