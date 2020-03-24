from flask import Blueprint

bp = Blueprint("api", __name__)

from web_backend.api import authentication, tokens, map_of_shop, main_routes