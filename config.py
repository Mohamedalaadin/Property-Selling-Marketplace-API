import os

class Config(object):

	# Database configuration
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Simple Cache Configuration
	CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')