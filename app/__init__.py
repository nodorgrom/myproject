from flask import Flask 
from .extensions import db
from .config import Config

from .routes import my_users

def create_app(config_class=Config):
	app = Flask(__name__)

	# Все что в config.py
	app.config.from_object(config_class)


	# 
	app.register_blueprint(my_users)

	db.init_app(app)

	with app.app_context():
		db.create_all()


	return app