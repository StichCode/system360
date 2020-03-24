from flask import request, jsonify
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import Role


@bp.route("/roles", methods=["GET"])
@jwt_required
def get_role_by():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = Role.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


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
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = Role.delete_by_id(args)
    print(d)
    if d is not None:
        return jsonify(message=f"No role with this id"), 201
    return jsonify(message=f"Role has been delete."), 201


@bp.route("/roles", methods=["PUT"])
@jwt_required
def edit_role():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="No data for edit"), 400
    try:
        role = Role.query.filter_by(id=data["id"]).first()
    except KeyError:
        return jsonify(message="Bad args"), 404
    if not role:
        return jsonify(message="No role with this id in database"), 404
    role = role.from_dict(data, True)
    if not role:
        return jsonify(message="Role can't be edit"), 401
    return jsonify(Role.query.filter_by(id=data["id"]).first().to_dict()), 201


def get_all_roles():
    roles = [role.to_dict() for role in Role.query.all()]
    if not roles:
        return jsonify(message="No roles in database"), 400
    return jsonify(roles), 200