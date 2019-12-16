from flask import json, request, Flask, Blueprint

dust = Blueprint('dust', __name__, url_prefix='/dust')