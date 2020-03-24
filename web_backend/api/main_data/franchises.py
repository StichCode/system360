from flask import request, jsonify
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import Franchise


@bp.route("/franchises", methods=["GET"])
@jwt_required
def get_franchise_by():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = Franchise.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


@bp.route("/franchises", methods=["POST"])
@jwt_required
def create_new_franchise():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="Bad args."), 400
    role = Franchise.from_dict(data)
    if not role:
        return jsonify(message="Franchise already exists"), 404
    return jsonify(message="Franchise has been create."), 200


@bp.route("/franchises", methods=["DELETE"])
@jwt_required
def delete_franchise():
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = Franchise.delete_by_id(args)
    if d is not None:
        return jsonify(message=f"No franchise with this id"), 201
    return jsonify(message=f"Franchise has been delete."), 201


@bp.route("/franchises", methods=["PUT"])
@jwt_required
def edit_franchise():
    data = request.get_json() or {}
    if not data or data.get("id") is None:
        return jsonify(message="Bad args."), 400
    return Franchise.global_edit(data)