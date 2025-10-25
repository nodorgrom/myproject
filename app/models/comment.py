from ..extensions import db

class MyComment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.Text())