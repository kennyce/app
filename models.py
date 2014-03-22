from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	sender = db.Column(db.String(15))
	content = db.Column(db.String(100))
	time = db.Column(db.DateTime)
	def __init__(self, sender, content):
		self.sender = sender
		self.content = content
		self.time = datetime.utcnow()
	def __repr__(self):
		return "<%s>" % self.content
		
	def timedel(self,t):
		return t-self.time
