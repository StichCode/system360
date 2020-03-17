from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend import db
from web_backend.api import bp
from web_backend.binder.users import users_by_role, user_delete, user_post, user_get
from web_backend.database.models import User


@bp.route('/test', methods=["POST"])
def test():
    # print([u.to_dict() for u in Shops.query.all()])

    return jsonify("Hello world"), 200


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


@bp.route("/users", methods=["GET"])
@jwt_required
def listing_users():
    users = user_get()
    if users:
        return jsonify(users), 200
    return jsonify(message="Unknown error."), 410


@bp.route("/users", methods=["POST"])
@jwt_required
def registration():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data or 'role' not in data \
            or 'franchise_id' not in data:
        return jsonify(message='Must include username, email, role and password fields'), 403
    if User.query.filter_by(username=data['username']).first():
        return jsonify(message='User with the same name already exists.'), 403
    if User.query.filter_by(email=data['email']).first():
        return jsonify(message='User with this e-mail already exists.'), 403
    user = user_post(data)
    print()
    db.session.add(user)
    db.session.commit()
    return jsonify(message="new user was be created"), 201


@bp.route("/users", methods=["DELETE"])
@jwt_required
def delete_user():
    try:
        user_id = int(request.args["id"])
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    user_delete(user_id)
    return jsonify(message=f"User {user_id} has been deleted"), 201