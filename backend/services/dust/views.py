from flask import json, request, Flask, Blueprint

dust = Blueprint('dust', __name__, url_prefix='/dust')


@dust.route('/')
def current():
    pass

@dust.route("/range")
def range():
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')