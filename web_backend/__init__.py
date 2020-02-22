from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from web_backend.config import Config

db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    from web_backend.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app


from web_backend.database import models
