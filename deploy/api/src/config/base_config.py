from datetime import timedelta
DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SECRET_KEY = "123456"
JSON_AS_ASCII = False
JWT_AUTH_HEADER_PREFIX = 'Bearer'
JWT_EXPIRATION_DELTA = timedelta(seconds=6000)