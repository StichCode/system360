from flask import Blueprint

bp = Blueprint("admin", __name__)

from web_backend.admin import franchises, users, object, shops, checkouts, tasks, subtasks