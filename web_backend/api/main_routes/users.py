import re

from flask import request, jsonify
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.binder.users import users_by_role
from web_backend.database.models import User


@bp.route("/users", methods=["GET"])
# @jwt_required
def get_users_by_role():
    data = request.args.to_dict()
    user = None
    if not data:
        return get_all_users()
    elif "id" in data:
        user = User.query.filter_by(id=data["id"]).first()
    elif "username" in data:
        user = User.query.filter_by(username=data["username"]).first()
    elif "email" in data:
        user = User.query.filter_by(email=data["email"]).first()
    elif "role" in data:
        users = users_by_role(data["role"])
        if users:
            return jsonify(users), 200
    if user is not None:
        return jsonify(user.to_dict()), 200
    return jsonify(message="No user in database with this data."), 400


@bp.route("/users", methods=["POST"])
@jwt_required
def new_user():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data or 'role' not in data \
            or 'franchise_id' not in data:
        return jsonify(message='Must include username, email, role and password fields'), 403
    if User.query.filter_by(username=data['username']).first():
        return jsonify(message='User with the same name already exists.'), 403
    if User.query.filter_by(email=data['email']).first():
        return jsonify(message='User with this e-mail already exists.'), 403
    if not re.findall(r"\S+@\S+", data['email']):
        return jsonify(message="Bad email"), 403
    user = User.from_dict(data)
    if not user:
        return jsonify(message="User already exists"), 403
    return jsonify(message="New user has been created"), 201


@bp.route("/users", methods=["DELETE"])
@jwt_required
def delete_user():
    user = request.args.get("id", type=int)
    if user is None:
        return jsonify(message="Bad parameters"), 401
    user = User.query.filter_by(id=user).first()
    if user is not None:
        user.delete_by_id()
        return jsonify(message=f"User {user} has been delete"), 201
    return jsonify(message="No user with this id"), 400


@bp.route("/users", methods=["PUT"])
@jwt_required
def edit_user():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="No data for edit"), 400
    try:
        user = User.query.filter_by(id=data["id"]).first()
    except KeyError:
        return jsonify(message="Bad args"), 404
    if not user:
        return jsonify(message="No user with this id in database"), 404
    user = user.from_dict(data, True)
    if not user:
        return jsonify(message="User can't be edit"), 401
    return jsonify(User.query.filter_by(id=data["id"]).first().to_dict()), 201


def get_all_users():
    users = [user.to_dict() for user in User.query.all()]
    if not users:
        return jsonify(message="No roles in database"), 400
    return jsonify(users), 200