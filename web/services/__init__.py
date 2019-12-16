from temperature.views import temperature
from dust.views import dust
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import smarthome_utils as h

app = Flask(__name__, instance_relative_config=True)
app.url_map.strict_slashes = False

config = h.read_configuration()
access_url = config["db"]["url"].split("//")
access_url = f'{access_url[0]}//{config["db"]["username"]}:{config["db"]["password"]}@{access_url[1]}'
app.config['SQLALCHEMY_DATABASE_URI'] = access_url

db = SQLAlchemy(app)

app.register_blueprint(dust)
app.register_blueprint(temperature)

db.create_all()


@app.route('/')
def index():
    response = app.response_class(
        response='{"application": "Smart home backend services", "env": "' +
        app.config['ENV'] + '", "debug": "' + str(app.config['DEBUG']) + '"}',
        mimetype="application/json"
    )
    return h.corsify_actual_response(response)
