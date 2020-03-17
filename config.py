import os


class Config(object):
    SECRET_KEY = "secret-key"
    JWT_SECRET_KEY = "very-secret-key"  # FIXME get this value from memcached
    CORS = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False