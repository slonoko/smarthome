from flask import jsonify, json, request, Flask
import datetime
from services import db

class Temperature(db.Model):

    __tablename__ = 'temperature'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Timestamp)
    temperature = db.Column(db.Double)
    humidity = db.Column(db.Double)

    def __init__(self):
        super().__init__()

    