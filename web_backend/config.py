import os


class Config(object):
    SECRET_KEY = ""
    JWT_SECRET_KEY = "secret-key"  # FIXME get this value from memcached
    SQLALCHEMY_DATABASE_URI = os.environ.setdefault("DATABASE_URL",
                                                    "postgresql+psycopg2://sys360:sys360@localhost:5432/system360")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
