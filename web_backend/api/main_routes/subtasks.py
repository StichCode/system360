from flask import jsonify, request
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import CheckoutSubTask


@bp.route("/subtasks", methods=["GET"])
@jwt_required
def subtasks():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = CheckoutSubTask.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


@bp.route("/subtasks", methods=["POST"])
@jwt_required
def new_subtasks():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="Bad args."), 400
    args = CheckoutSubTask.from_dict(data)
    if not args:
        return jsonify(message="SubTask already exists"), 404
    return jsonify(message="SubTask has been create."), 200


@bp.route("/subtasks", methods=["DELETE"])
@jwt_required
def delete_subtasks():
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = CheckoutSubTask.delete_by_id(args)
    if d is not None:
        return jsonify(message=f"No subTask with this id"), 201
    return jsonify(message=f"SubTask has been delete."), 201