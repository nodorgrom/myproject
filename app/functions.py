import os.path
import secrets
from flask import current_app
from PIL import Image


def save_picture(pic):
	random_hex = secrets.token_hex(14)
	_, f_ext = os.path.splitext(pic.filename)
	pic_filename = random_hex + f_ext
	pic_path = os.path.join(current_app.config['SERVER_PATH'], pic_filename)

	output_size = (125, 125)
	img = Image.open(pic)
	img.thumbnail(output_size)
	img.save(pic_path)

	return pic_filename
