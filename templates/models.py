import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class detl(db.model):
    __tablename__="Nptel"
    regno=db.Column(db.Integer)
