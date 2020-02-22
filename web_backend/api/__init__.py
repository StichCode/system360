from flask import Blueprint

bp = Blueprint("api", __name__)

from web_backend.api import authentication
