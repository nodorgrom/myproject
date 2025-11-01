from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField, FileField, BooleanField
from .models.user import MyUsers


class RegistrationForm(FlaskForm):
	user_name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=100)])
	login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=24)])
	password = PasswordField('Пароль', validators=[DataRequired()])
	confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
	avatar = FileField('Аватар', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
	submit = SubmitField('Зарегистрироваться')


	def validate_login(self, login):
		user = MyUsers.query.filter_by(login=login.data).first()

		if user:
			raise ValidationError(f"Попробуйте другой логин")




class LoginForm(FlaskForm):
	login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Пароль', validators=[DataRequired()])
	remember = BooleanField('Запомнить меня')
	submit = SubmitField('Войти')
