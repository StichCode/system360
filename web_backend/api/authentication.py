import bcrypt
from flask import request, jsonify

from web_backend import db, auth
from web_backend.api import bp
from web_backend.binder.methods_user import verify_password, users_by_role
from web_backend.database.models import User, Role
from flask_user import roles_required


@bp.route("/test", methods=["GET"])
def test():

    # user = User(
    #     username="mana",
    #     email="sys36s@sys0.com",
    #     password_hash=(bcrypt.hashpw(b"sys360", bcrypt.gensalt(15))).decode('UTF-8'),
    #     first_name="sys0",
    #     last_name="sys0",
    #     role=1
    # )
    # db.session.add(user)
    # db.session.commit()
    users = users_by_role("Manager")
    print(users)
    return f"<h1>Hello World! </h1>"


@bp.route("/auth", methods=["POST"])
def login():
    data = request.get_json() or {}
    if verify_password(**data):
        return jsonify({"status": "200", "role": "Admin"})


@bp.route("/users", methods=["GET"])
def get_users_by_role():
    role_id = request.args["roleId"]
    users = users_by_role(role_id)
    if users:
        return jsonify(users)
    return jsonify(status=400, message="No users with this roles.")

