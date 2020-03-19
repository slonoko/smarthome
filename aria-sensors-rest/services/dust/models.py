from flask import jsonify, request, Flask
import datetime
from services import db

class Dust(db.Model):

    __tablename__ = 'dust'

    id = db.Column(db.Integer, primary_key=True)
    startdate = db.Column(db.DateTime)
    enddate = db.Column(db.DateTime)
    value = db.Column(db.Float)
    voltage = db.Column(db.Float)
    density = db.Column(db.Float)

    def __init__(self):
        super().__init__()

    def __json__(self):
        json = {
            'id': self.id,
            'value': self.value,
            'voltage': self.voltage,
            'density': self.density,
            'enddate': self.enddate,
            'startdate': self.startdate
        }

        return json