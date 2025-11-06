import os

from flask_assets import Bundle

from .functions import recursive_flatten_iterator





def get_bundle(route, tmpl, ext, paths, type=False):
	if route and tmpl and ext:
		return {
			'instance': Bundle(*paths, output=get_path(route, tmpl, ext, type), filters=get_filter(ext)),
			'name': get_filename(route, tmpl, ext, type),
			'dir': os.getcwd()
		}


def register_bundle(assets, bundle):
	assets.register(bundle['name'], bundle['instance'])
	return f"Bundle {bundle['name']} registered success!"


def register_bundles(assets, bundles):
	for i in recursive_flatten_iterator(bundles):
		for bundle in i:
			register_bundle(assets, bundle)


def get_filename(route, tmpl, ext, type):
	if type:
		return f"{route}_{tmpl}_{ext}_defer"
	else:
		return f"{route}_{tmpl}_{ext}"


def get_path(route, tmpl, ext, type):
	if type:
		return f"gen/{route}/{tmpl}/defer.{ext}"
	else:
		return f"gen/{route}/{tmpl}/main.{ext}"


def get_filter(ext):
	return f"{ext}min"




bundles = {
	"post": {
		"all": {},
		"create": {},
		"edit": {},
	},
	"user": {
		"login": {},
		"login_form_content": {},
		"profile": {},
		"register": {},
	},
}



