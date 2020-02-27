from flask import Blueprint
from flask_cors import CORS

bp = Blueprint("admin", __name__)

CORS(bp)

from web_backend.admin import franchises, users, object, shops