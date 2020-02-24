import unittest

from main import app


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://test_sys360:test_sys360@localhost:5432/test_system360"

