from flask import Blueprint
from flask_cors import CORS

bp = Blueprint("admin", __name__)

CORS(bp)  # FIXME NOT FOR PRODUCTION

from web_backend.admin import franchises, users, object, shops