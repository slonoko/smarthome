from flask import json, request, Flask, Blueprint, current_app
from services.dust.models import Dust
import smarthome_utils as h
import datetime

dust = Blueprint('dust', __name__, url_prefix='/dust')

def toDate(dateString): 
    return datetime.datetime.strptime(dateString, "%d.%m.%Y-%H:%M").date()

@dust.route('/')
def current():
    latest_dust = Dust.query.order_by(Dust.enddate.desc()).first()
    latest_dust = latest_dust if latest_dust is not None else Dust()
    return h.getResponse(current_app,latest_dust.to_json())

@dust.route("/range")
def range():
    from_date = request.args.get('from_date', default = datetime.date.today(), type = toDate)
    to_date = request.args.get('to_date', default = datetime.date.today(), type = toDate)
    print(Dust.query.filter(Dust.startdate.between(from_date,  to_date)).order_by(Dust.startdate.desc()))
    list_dusts = Dust.query.filter(Dust.startdate.between(from_date,  to_date)).order_by(Dust.startdate.desc()).all()
    print(list_dusts)
    return h.getResponse(current_app,list_dusts[0].to_json())