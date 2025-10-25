from datetime import datetime
from ..extensions import db


class MyUsers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	role = db.Column(db.String(50), default='user')
	avatar = db.Column(db.String(250))
	user_name = db.Column(db.String(50))
	login = db.Column(db.String(50))
	password = db.Column(db.String(250))
	date = db.Column(db.DateTime, default=datetime.utcnow)


