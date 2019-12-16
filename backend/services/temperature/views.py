from flask import json, request, Flask, Blueprint

temperature = Blueprint('temperature', __name__, url_prefix='/temperature')