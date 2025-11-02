from datetime import datetime
from ..extensions import db

class MyPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	teacher = db.Column(db.Integer, db.ForeignKey('my_users.id', ondelete='CASCADE'))
	subject = db.Column(db.String(250))
	student = db.Column(db.Integer)
	date = db.Column(db.DateTime, default=datetime.utcnow)