from datetime import datetime
from ..extensions import db

class MyPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	price = db.Column(db.String(250))
	name = db.Column(db.String(250))
	count = db.Column(db.String(250))
	date = db.Column(db.DateTime, default=datetime.utcnow)