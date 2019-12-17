from flask import jsonify, json, request, Flask
import datetime
from services import db

class Dust(db.Model):

    __tablename__ = 'dust'

    id = db.Column(db.Integer, primary_key=True)
    startdate = db.Column(db.Timestamp)
    enddate = db.Column(db.Timestamp)
    value = db.Column(db.Double)
    voltable = db.Column(db.Double)
    density = db.Column(db.Double)

    def __init__(self):
        super().__init__()

    