from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.database.models import Role


@bp.route("/roles", methods=["GET"])
@jwt_required
def get_role_by():
    role = request.args.get("id", type=int) or request.args.get("name", type=str)
    if role is None:
        return get_all_roles()
    if isinstance(role, int):
        role = Role.query.filter_by(id=role).first()
    else:
        role = Role.query.filter_by(name=role).first()
    if role is not None:
        return jsonify(role.to_dict()), 200
    return jsonify(status=400, message="No users with this roles.")


@bp.route("/roles", methods=["POST"])
@jwt_required
def create_new_role():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="No data for create role"), 400
    role = Role.from_dict(data)
    if not role:
        return jsonify(message="Role already exists"), 404
    return jsonify(Role.query.filter_by(name=data["name"]).first().to_dict()), 200


@bp.route("/roles", methods=["DELETE"])
@jwt_required
def delete_role():
    try:
        role = request.args["id"]
    except BadRequestKeyError:
        return 400
    role = Role.query.filter_by(id=role).first()
    if role is not None:
        role.delete_by_id()
        return jsonify(message=f"Role {role} has been delete"), 201
    return jsonify(message="No role with this id"), 400


@bp.route("/roles", methods=["PUT"])
@jwt_required
def edit_role():
    try:
        data = request.get_json() or {}
    except BadRequestKeyError:
        return jsonify(message="No data for edit"), 400
    role = Role.query.get_or_404(data["id"])
    role = role.from_dict(data, True)
    if not role:
        return jsonify(message="Role can't be edit"), 401
    return jsonify(Role.query.filter_by(id=data["id"]).first().to_dict()), 201


def get_all_roles():
    roles = [role.to_dict() for role in Role.query.all()]
    if not roles:
        return jsonify(message="No roles in database"), 400
    return jsonify(roles), 200