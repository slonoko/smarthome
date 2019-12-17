from flask import jsonify, json, request, Flask
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

    