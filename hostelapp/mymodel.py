import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Column, PrimaryKeyConstraint
# from sqlalchemy.orm import backref
# from sqlalchemy.sql.schema import ForeignKey
# from hostelapp import db

db = SQLAlchemy()

class Hostel(db.Model):
    __tabelname__='hostel'
    hostel_id = db.Column(db.Integer(), primary_key = True,autoincrement = True)
    hostel_name = db.Column(db.String(255), nullable = False)
    hostel_desc = db.Column(db.String(255), nullable = False)
    hostel_type = db.Column(db.Enum('Female','Male','Mixed'))
    hostel_dateadded = db.Column(db.DateTime,default=datetime.datetime.utcnow)

class Merchant(db.Model):
    __tabelname__='merchant'
    mer_id = db.Column(db.Integer(), primary_key = True,autoincrement = True)
    mer_username = db.Column(db.String(50), nullable=False)
    mer_pwd = db.Column(db.String(55), nullable=False)