from flask import json, current_app

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def getResponse(respJson):
    resp = current_app.response_class(
        response=json.dumps(respJson),
        mimetype="application/json"
    )
    resp = _corsify_actual_response(resp)
    return resp