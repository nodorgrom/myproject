from flask import Blueprint
from ..extensions import db
from ..models.comment import MyComment

my_comment = Blueprint('my_comment', __name__)



@my_comment .route('/my_comments/<message>')
def create_comment(message):
	my_comment = MyComment(message=message)
	db.session.add(my_comment)
	db.session.commit()
	return f"comment created!"

