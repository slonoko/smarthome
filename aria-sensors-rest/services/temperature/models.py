from flask import jsonify, json, request, Flask
import datetime
from services import db

class Temperature(db.Model):

    __tablename__ = 'temperature'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)

    def __init__(self):
        super().__init__()

    def __json__(self):
        json = {
            'id': self.id,
            'timestamp': self.timestamp,
            'temperature': self.temperature,
            'humidity': self.humidity
        }

        return json
