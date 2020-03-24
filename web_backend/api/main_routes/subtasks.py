from flask import jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

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
    if not data or "task" not in data \
            or "title" not in data:
        return jsonify(message="Bad parameters"), 401
    return jsonify(message=f"Subtask  has been created"), 201


@bp.route("/subtasks", methods=["DELETE"])
@jwt_required
def delete_subtasks():
    try:
        task_id = int(request.args["id"])
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    # subtasks_delete(task_id)
    return jsonify(message=f"Subtask {task_id} has been delete"), 201