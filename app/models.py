from .extensions import db

class MyUsers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(50))


