from flask import Blueprint
from ..extensions import db
from ..models.post import MyPost

my_post = Blueprint('my_post', __name__)



@my_post.route('/my_post/<subject>')
def create_subject(subject):
	my_post = MyPost(subject=subject)
	db.session.add(my_post)
	db.session.commit()
	return f"Post {my_post} created!"

