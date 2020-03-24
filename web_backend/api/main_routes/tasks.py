from flask import jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

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
    if not data or "object_id" not in data \
            or "checkout" not in data\
            or "status" not in data\
            or "title" not in data:
        return jsonify(message="Bad parameters"), 401
    return jsonify(message=f"checkout  has been created"), 201


@bp.route("/tasks", methods=["DELETE"])
@jwt_required
def delete_tasks():
    try:
        task_id = int(request.args["id"])
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    return jsonify(message="Franchise hs been delete"), 201