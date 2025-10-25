from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post import MyPost

my_post = Blueprint('my_post', __name__)



@my_post.route('/post/create', methods=['POST', 'GET'])
def create():
	if request.method == 'POST':
		teacher = request.form.get('teacher')
		subject = request.form.get('subject')
		student = request.form.get('student')

		post = MyPost(teacher=teacher, subject=subject, student=student)

		try:
			db.session.add(post)	
			db.session.commit()
			return redirect('/')
		except Exception as e:
			print(str(e))
			raise e

	else:
		return render_template('post/create.html')
