import re

from flask import request, jsonify
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import User


@bp.route("/users", methods=["GET"])
@jwt_required
def get_users_by_role():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = User.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


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
    if not data:
        return jsonify(message="Bad args."), 400
    args = User.from_dict(data)
    if not args:
        return jsonify(message="User already exists"), 404
    return jsonify(message="User has been create."), 200


@bp.route("/users", methods=["DELETE"])
@jwt_required
def delete_user():
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = User.delete_by_id(args)
    if d is not None:
        return jsonify(message=f"No user with this id"), 201
    return jsonify(message=f"User has been delete."), 201


@bp.route("/users", methods=["PUT"])
@jwt_required
def edit_user():
    data = request.get_json() or {}
    if not data and data.get("id") is not None:
        return jsonify(message="Bad args."), 400
    return User.global_edit(data)