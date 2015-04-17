from flask import Flask
from flaskext.mysql import MySQL
from flask.ext.sqlalchemy import SQLAlchemy
import json

#Setups 
app = Flask(__name__)
app.config.from_object('config')
mysql = MySQL()
mysql.init_app(app)
cursor = mysql.connect().cursor()
db = SQLAlchemy(app)

#Static information
idToDataName = json.load(open("app/maps/idToDataName.json",'r'))
champInformation = json.load(open("app/maps/champ_data.json", "r"))

from app import views, models, UrfDataAggregator

