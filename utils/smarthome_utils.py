import json
import sys
import datetime
import os


def params():
    properties = ['CX_SPARK_URL', 'CX_KAFKA_URL', 'CX_DB_URL',
                  'CX_DB_USER', 'CX_DB_PWD', 'CX_DB_DRIVER', 'CX_DB_PREFIX']
    return properties


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
