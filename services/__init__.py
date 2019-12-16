import os
from flask import Flask
import api.utils as h
from flask_sqlalchemy import SQLAlchemy # https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
from smarthome_utils import read_configuration

app = Flask(__name__, instance_relative_config=True)
app.url_map.strict_slashes = False

config = read_configuration()

app.config['SQLALCHEMY_DATABASE_URI'] = config["db"]["url"]
db = SQLAlchemy(app) 

from api.questions.views import questions
from api.scores.views import scores
app.register_blueprint(questions)
app.register_blueprint(scores)

db.create_all() 

@app.route('/')
def index():
    response = app.response_class(
    response = '{"application": "Assessment backend API", "env": "' + app.config['ENV'] + '", "debug": "' + str(app.config['DEBUG']) + '"}',
        mimetype = "application/json"
    )
    return h._corsify_actual_response(response)