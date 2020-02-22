import os


class Config(object):
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = os.environ.setdefault("DATABASE_URL",
                                                    "postgresql+psycopg2://sys360:sys360@localhost:5432/system360")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
