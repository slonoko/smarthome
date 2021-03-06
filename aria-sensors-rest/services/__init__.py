import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import utils as h

app = Flask(__name__, instance_relative_config=True)
app.url_map.strict_slashes = False

db_prefix = 'postgresql+psycopg2'
db_user = os.getenv("CX_DB_USER")
db_pwd = os.getenv("CX_DB_PWD")
db_ip = f'aria-storage:5432/{os.getenv("CX_DB_NAME")}'

access_url = f'{db_prefix}://{db_user}:{db_pwd}@{db_ip}'
app.config['SQLALCHEMY_DATABASE_URI'] = access_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from services.dust.views import dust
from services.temperature.views import temperature

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
