from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from ..extensions import db
from ..models.post import MyPost
from ..models.user import MyUsers
from ..forms import StudentForm

my_post = Blueprint('my_post', __name__)


@my_post.route('/', methods=['POST', 'GET'])
def all():
	posts = MyPost.query.order_by(MyPost.date.desc()).all()
	return render_template('post/all.html', posts=posts, user=MyUsers)


@my_post.route('/post/create', methods=['POST', 'GET'])
@login_required
def create():
	form = StudentForm()
	form.student.choices = [ s.user_name for s in MyUsers.query.filter_by(role='user')]

	if request.method == 'POST':
		subject = request.form.get('subject')
		student = request.form.get('student')

		student_id = MyUsers.query.filter_by(user_name=student).first().id

		post = MyPost(teacher=current_user.id, subject=subject, student=student_id)

		try:
			db.session.add(post)	
			db.session.commit()
			return redirect('/')
		except Exception as e:
			print(str(e))

	else:
		return render_template('post/create.html', form=form)


@my_post.route('/post/<int:id>/edit', methods=['POST', 'GET'])
@login_required
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



@my_post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
@login_required
def delete(id):
	post = MyPost.query.get(id)
	print(type(post))
	print(post)

	try:
		db.session.delete(post)
		db.session.commit()
		return redirect('/')
	except Exception as e:
		print(str(e))
		return str(e)
