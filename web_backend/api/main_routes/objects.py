from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.database.models import Object


@bp.route("/objects", methods=["GET"])
# @jwt_required
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
        jsonify(message="Bad data"), 401
    return jsonify(message="Надо проверить работает ли, но позже"), 200


@bp.route("/objects", methods=["DELETE"])
@jwt_required
def del_object():
    try:
        obj_id = request.args["objectID"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    # object_delete(obj_id)
    return jsonify(message=f"Object {obj_id} has been deleted"), 201


@bp.route("/objects", methods=["PUT"])
@jwt_required
def change_object():
    return jsonify(messag="ЕЩЁ НЕ РАБОТАЕТ ВОВА"), 200


