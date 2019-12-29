import json
import sys
import datetime
import os

def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def getResponse(current_app, respJson):
    resp = current_app.response_class(
        response=json.dumps(respJson, indent=4, sort_keys=True, default=str),
        mimetype="application/json"
    )
    resp = corsify_actual_response(resp)
    return resp


def to_date(dateString):
    return datetime.datetime.strptime(dateString, "%d.%m.%Y-%H:%M")
