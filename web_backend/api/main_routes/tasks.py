from flask import jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp


@bp.route("/tasks", methods=["GET"])
@jwt_required
def tasks():
    tasks_all = ...
    if tasks_all:
        return jsonify(tasks_all), 200
    return jsonify(message="No tasks in database."), 400


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