from flask import Blueprint

bp = Blueprint("api", __name__)

from web_backend.api import authentication, tokens, users, shops, map_of_shop, keys