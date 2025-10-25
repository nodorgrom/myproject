from flask import Flask 
from .extensions import db
from .config import Config

from .routes.user import my_users
from .routes.post import my_post
from .routes.comment import my_comment


def create_app(config_class=Config):
	app = Flask(__name__)

	# Все что в config.py
	app.config.from_object(config_class)


	# 
	app.register_blueprint(my_users)
	app.register_blueprint(my_post)
	app.register_blueprint(my_comment)

	db.init_app(app)

	with app.app_context():
		db.create_all()


	return app