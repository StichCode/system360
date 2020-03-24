from flask import jsonify, request
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import CheckoutTask


@bp.route("/tasks", methods=["GET"])
@jwt_required
def tasks():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = CheckoutTask.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


@bp.route("/tasks", methods=["POST"])
@jwt_required
def new_tasks():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="Bad args."), 400
    args = CheckoutTask.from_dict(data)
    if not args:
        return jsonify(message="Task already exists"), 404
    return jsonify(message="Task has been create."), 200


@bp.route("/tasks", methods=["DELETE"])
@jwt_required
def delete_tasks():
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = CheckoutTask.delete_by_id(args)
    if d is not None:
        return jsonify(message=f"No task with this id"), 201
    return jsonify(message=f"Task has been delete."), 201


@bp.route("/tasks", methods=["PUT"])
@jwt_required
def edit_task():
    data = request.get_json() or {}
    if not data or data.get("id") is None:
        return jsonify(message="Bad args."), 400
    return CheckoutTask.global_edit(data)