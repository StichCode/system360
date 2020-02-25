from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend import db
from web_backend.api import bp
from web_backend.binder.user import users_by_role, hash_pw, new_user
from web_backend.database.models import User


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
    data = request.get_json() or {}

    if 'username' not in data or 'email' not in data or 'password' not in data or 'role' not in data \
            or 'franchise_id' not in data:
        return jsonify(message='Must include username, email, role and password fields'), 403
    if User.query.filter_by(username=data['username']).first():
        return jsonify(message='User with the same name already exists.'), 403
    if User.query.filter_by(email=data['email']).first():
        return jsonify(message='User with this e-mail already exists.'), 403

    user = new_user(data)
    db.session.add(user)
    db.session.commit()

    return jsonify(message="new user was be created"), 201
