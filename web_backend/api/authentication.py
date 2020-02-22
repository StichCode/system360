from flask import request, jsonify

from web_backend import db, auth
from web_backend.api import bp
from web_backend.api.errors import error_response
from web_backend.binder.methods_user import verify_password, users_by_role
from web_backend.database.models import User, Role
from flask_user import roles_required


@bp.route("/test", methods=["GET"])
def test():
    return f"<h1>Hello World! </h1>"


@bp.route("/auth", methods=["POST"])
@auth.verify_password
def login():
    data = request.get_json() or {}
    response = verify_password(data)
    if response is not None:
        return jsonify(response)
    return error_response(401)


@bp.route("/users", methods=["GET"])
@auth.login_required
def get_users_by_role():
    role_id = request.args["roleId"]
    users = users_by_role(role_id)
    if users:
        return jsonify(users)
    return jsonify(status=400, message="No users with this roles.")

