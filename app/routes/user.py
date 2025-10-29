from flask import Blueprint, render_template, redirect, flash
from ..forms import RegistrationForm
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

			return redirect('/')
		else:
			flash(f"Ошибка регистрации: {form.user_name.data} {form.login.data} {form.avatar.data}", "danger")
			print('Ошибка регистрации')

	return render_template('user/register.html', form=form)



