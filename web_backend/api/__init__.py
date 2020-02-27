from flask import Blueprint
from flask_cors import CORS

bp = Blueprint("api", __name__)

CORS(bp)  # FIXME NOT FOR PRODUCTION

from web_backend.api import authentication, tokens, users, shops, map_of_shop