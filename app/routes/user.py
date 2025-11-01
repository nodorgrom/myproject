from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_user
from ..forms import RegistrationForm, LoginForm
from ..extensions import db, bcrypt
from ..models.user import MyUsers
from ..functions import save_picture

my_users = Blueprint('my_users', __name__)



@my_users.route('/user/register', methods=['POST', 'GET'])
def register_user():
	form = RegistrationForm()

	if form.user_name.data and form.login.data and form.password.data != "":
		if form.validate_on_submit():
			hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			avatar_filename = save_picture(form.avatar.data)
			user = MyUsers(user_name=form.user_name.data, login=form.login.data, avatar=avatar_filename, password=hashed_password)

			db.session.add(user)
			db.session.commit()

			flash(f"Добро пожаловать, {form.user_name.data} ({form.login.data})!", "success")

			return redirect(url_for('user.login'))
		else:
			flash(f"Ошибка регистрации", "danger")
			print('Ошибка регистрации')

	return render_template('user/register.html', form=form)


@my_users.route('/user/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = MyUsers.query.filter_by(login=form.login.data).first()

		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			for i in form:
				print(i)
			flash(f"Добро пожаловать, {form.login.data}!", "success")

			return redirect(next_page) if next_page else redirect(url_for('my_post.all'))
		else:
			flash(f"Ошибка авторизации. Проверьте email и пароль!", "danger")

	return render_template('user/login.html', form=form)


