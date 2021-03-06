from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    if app.config.get("CORS"):
        cors.init_app(app, resources={r"/*": {"origins": "*"}})

    from web_backend.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


from web_backend.database import models
from web_backend import files