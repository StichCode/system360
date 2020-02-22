import bcrypt
from flask import request, jsonify

from web_backend import db, auth
from web_backend.api import bp
from web_backend.binder.methods_user import verify_password
from web_backend.database.models import User, Role
from flask_user import roles_required


@bp.route("/test", methods=["GET"])
def test():
    # user = User(
    #     username="sys360",
    #     email="sys360@sys360.com",
    #     password_hash=(bcrypt.hashpw(b"sys360", bcrypt.gensalt(15))).decode('UTF-8'),
    #     first_name="sys360",
    #     last_name="sys360",
    #     role=2
    # )
    # db.session.add(user)
    # db.session.commit()
    return f"<h1>Hello World! </h1>"


@bp.route("/auth", methods=["POST"])
def login():
    data = request.get_json() or {}
    if verify_password(**data):
        return jsonify({"status": "200", "role": "Admin"})


@bp.route("/users?roleId=")
def get_users_by_role():
    role_id = request.args.get("roleId", type=int)


