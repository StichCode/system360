from flask import request, jsonify
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import Object


@bp.route("/objects", methods=["GET"])
@jwt_required
def get_all_objects():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = Object.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


@bp.route("/objects", methods=["POST"])
@jwt_required
def create_object():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="Bad args."), 400
    args = Object.from_dict(data)
    if not args:
        return jsonify(message="Object already exists"), 404
    return jsonify(message="Object has been create."), 200


@bp.route("/objects", methods=["DELETE"])
@jwt_required
def del_object():
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = Object.delete_by_id(args)
    if d is not None:
        return jsonify(message=f"No object with this id"), 201
    return jsonify(message=f"Object has been delete."), 201


@bp.route("/objects", methods=["PUT"])
@jwt_required
def edit_object():
    data = request.get_json() or {}
    if not data or data.get("id") is None:
        return jsonify(message="Bad args."), 400
    return Object.global_edit(data)