import os


class BaseConfig(object):
    SECRET_KEY = "secret-key"
    JWT_SECRET_KEY = "very-secret-key"  # FIXME get this value from memcached
    CORS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL")
    TESTING = True
    CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    CORS = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PRODUCTION_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
