from flask import Blueprint, render_template, redirect
from ..forms import RegistrationForm
from ..extensions import db
from ..models.user import MyUsers

my_users = Blueprint('my_users', __name__)



@my_users.route('/user/register', methods=['POST', 'GET'])
def register_user():
	form = RegistrationForm()

	if form.validate_on_submit():
		# TODO:
		# хэшировать пароль и сохранять в БД
		# 3:50:05
		pass
		# print(form.user_name.data)
		# print(form.password.data)
		# print(form.avatar.data)
		return redirect('/')
	else:
		print('Ошибка регистрации')

	return render_template('user/register.html', form=form)



