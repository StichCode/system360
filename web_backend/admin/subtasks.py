from flask import jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.admin import bp
from web_backend.binder.subtasks import subtasks_get_all, subtasks_post, subtasks_delete


@bp.route("/subtasks", methods=["GET"])
@jwt_required
def subtasks():
    tasks_all = subtasks_get_all()
    if tasks_all:
        return jsonify(tasks_all), 201
    return jsonify(message="No tasks in database."), 400


@bp.route("/subtasks", methods=["POST"])
@jwt_required
def new_subtasks():
    data = request.get_json() or {}
    if not data or "task" not in data \
            or "title" not in data:
        return jsonify(message="Bad parameters"), 401
    return jsonify(message=f"Subtask {subtasks_post(data)} has been created"), 201


@bp.route("/subtasks", methods=["DELETE"])
@jwt_required
def delete_subtasks():
    try:
        task_id = int(request.args["id"])
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    subtasks_delete(task_id)
    return jsonify(message=f"Subtask {task_id} has been delete"), 201