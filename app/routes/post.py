from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post import MyPost

my_post = Blueprint('my_post', __name__)


@my_post.route('/', methods=['POST', 'GET'])
def all():
	posts = MyPost.query.order_by(MyPost.date.desc()).all()
	return render_template('post/all.html', posts=posts)


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

	else:
		return render_template('post/create.html')


@my_post.route('/post/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
	post = MyPost.query.get(id)


	if request.method == 'POST':
		post.teacher = request.form.get('teacher')
		post.subject = request.form.get('subject')
		post.student = request.form.get('student')

		try:
			db.session.commit()
			return redirect('/')
		except Exception as e:
			print(str(e))

	else:
		return render_template('post/edit.html', post=post)

