from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
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

			return redirect(url_for('my_users.login'))
		else:
			flash(f"Ошибка регистрации", "danger")
			print('Ошибка регистрации')

	return render_template('user/register.html', form=form)


@my_users.route('/user/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # ... (логика входа остается прежней) ...
        user = MyUsers.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"Добро пожаловать, {form.login.data}!", "success")
            # После успешного входа делаем полное перенаправление
            return redirect(next_page) if next_page else redirect(url_for('my_post.all'))
        else:
            flash(f"Ошибка авторизации. Проверьте email и пароль!", "danger")
            # При ошибке делаем полное перенаправление обратно на главную
            return redirect(url_for('my_post.all')) 

    # Если запрос GET и это не AJAX-запрос, то рендерим обычную страницу входа (на всякий случай)
    if not request.headers.get("X-Requested-With") == "Fetch":
         return render_template('user/login.html', form=form)

@my_users.route('/user/login/modal', methods=['GET'])
def login_modal():
    form = LoginForm()
    # Рендерим ТОЛЬКО содержимое формы без наследования base.html
    return render_template('user/login_form_content.html', form=form)


@my_users.route('/user/logout', methods=['POST', 'GET'])
def logout():
	logout_user()
	return redirect(url_for('my_post.all'))



@my_users.route('/user/profile', methods=['POST', 'GET'])
@login_required
def profile():
	return render_template('user/profile.html', user=current_user)











