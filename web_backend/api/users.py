from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend import db
from web_backend.api import bp
from web_backend.binder.methods_user import users_by_role, hash_pw
from web_backend.database.models import User, Role


@bp.route("/users", methods=["GET"])
@jwt_required
def get_users_by_role():
    # current_user = get_jwt_identity()
    try:
        role = request.args["role"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    users = users_by_role(role)
    if users:
        return jsonify(users)
    return jsonify(status=400, message="No users with this roles.")


@bp.route("/reg", methods=["POST"])
def registration():
    # FIXME сделать проверку на существующий юзернейм и почту
    data = request.get_json() or {}
    if not data:
        return jsonify(message="No any data for registration"), 403
    flag = [key for key in list(data.keys()) if key not in
            ["username", "password", "email", "first_name", "last_name", "role"]]  # FIXME without phone key
    if flag:
        return jsonify(message="No any data for registration"), 403
    role = Role.query.filter_by(name=data["role"]).first()
    phone = ""
    try:
        phone = data["phone"]
    except KeyError:
        pass
    user = User(
        username=data["username"],
        email=data["email"],
        phone=phone,
        password_hash=hash_pw(data["password"]),
        first_name=data["first_name"],
        last_name=data["last_name"],
        role=role.id
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(message="new user was be created"), 201
