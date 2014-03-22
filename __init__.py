from flask import Flask
from models import db
from flask.ext.restful.utils import cors
from restapi import api, Tv

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
with app.app_context():
	db.create_all()
api.init_app(app)
api.decorators=[cors.crossdomain(origin='*')]
from app import utils
