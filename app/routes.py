from flask import Blueprint
from .extensions import db
from .models import MyUsers

my_users = Blueprint('my_users', __name__)



@my_users.route('/my_users/<name>')
def create_user(name):
	my_users = MyUsers(user_name=name)
	db.session.add(my_users)
	db.session.commit()
	return f"User {name} created!"

