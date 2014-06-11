try:
	from setuptools import setup
except ImportError:
	from distutile.core import setup

config = {
	'description': "jelly's project",
	'author': 'jelly',
	'url': "let's decide this later",
	'download_url': 'the same as above',
	'author_email': 'jelly329@126.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'my first python project'
}

setup(**config)
