from flask import Blueprint, render_template, request, redirect, flash, url_for
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
    post = MyPost.query.get_or_404(id) # Используем get_or_404 для безопасности

    form = StudentForm()
    
    # 1. Заполняем choices кортежами (ID, Имя)
    users = MyUsers.query.filter_by(role='user').all()
    form.student.choices = [(str(s.id), s.user_name) for s in users] # ID должен быть строкой для SelectField

    # 2. Если это GET-запрос (первое открытие страницы), устанавливаем текущее значение по умолчанию
    if request.method == 'GET':
        # Устанавливаем ID текущего студента как значение по умолчанию
        form.student.data = str(post.student)

    # 3. Обработка POST-запроса
    if request.method == 'POST':
        # Проверяем валидацию формы перед обработкой
        if form.validate_on_submit():
            post.subject = request.form.get('subject') # Это поле вы не показывали, но оно здесь

            # Получаем ID из формы (он придет как строка, но SQL Alchemy его преобразует)
            selected_student_id = request.form.get('student') 
            post.student = selected_student_id

            try:
                db.session.commit()
                flash("Запись успешно обновлена!", "success")
                return redirect(url_for('my_post.all'))
            except Exception as e:
                db.session.rollback() # Откатываем изменения в случае ошибки
                print(str(e))
                flash("Произошла ошибка при сохранении в базу.", "danger")
        else:
             flash("Ошибка валидации формы.", "danger")
             
    # Если GET или POST с ошибками валидации, рендерим шаблон
    return render_template('post/edit.html', post=post, form=form)


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
