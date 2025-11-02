from datetime import datetime
from ..extensions import db, login_manager
from flask_login import UserMixin
from .post import MyPost


@login_manager.user_loader
def load_user(user_id):
	return MyUsers.query.get(int(user_id))


class MyUsers(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	posts = db.relationship(MyPost, backref='author')
	role = db.Column(db.String(50), default='user')
	avatar = db.Column(db.String(250))
	user_name = db.Column(db.String(50))
	login = db.Column(db.String(50))
	password = db.Column(db.String(250))
	date = db.Column(db.DateTime, default=datetime.utcnow)


