import argparse, json, sys

def read_configuration():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",  nargs='+', help="Configuration file in json format")
    args = parser.parse_args()
    json_file = args.config[0]
    config = {}
    if json_file:
        with open(json_file) as f:
            config = json.load(f)
    return config

def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def getResponse(current_app, respJson):
    resp = current_app.response_class(
        response=json.dumps(respJson),
        mimetype="application/json"
    )
    resp = corsify_actual_response(resp)
    return resp