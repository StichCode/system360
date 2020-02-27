from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.binder.users import users_by_role


@bp.route("/users", methods=["GET"])
@jwt_required
def get_users_by_role():
    try:
        role = request.args["role"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    users = users_by_role(role)
    if users:
        return jsonify(users)
    return jsonify(status=400, message="No users with this roles.")