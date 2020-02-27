from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.admin import bp
from web_backend.binder.object import object_delete, object_post, object_get


@bp.route("/objects", methods=["GET"])
@jwt_required
def get_all_objects():
    objects = object_get()
    if objects:
        return jsonify(objects), 201
    return jsonify(status=400, message="No objects in database.")


@bp.route("/objects", methods=["POST"])
@jwt_required
def create_object():
    data = request.get_json() or {}
    if not data:
        jsonify(message="Bad data"), 401
    object_post(data)
    return jsonify(message="Надо проверить работает ли, но позже"), 200


@bp.route("/objects", methods=["DELETE"])
@jwt_required
def del_object():
    try:
        obj_id = request.args["objectID"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    object_delete(obj_id)
    return jsonify(message=f"Object {obj_id} has been deleted"), 201


@bp.route("/objects", methods=["PUT"])
@jwt_required
def change_object():
    return jsonify(messag="ЕЩЁ НЕ РАБОТАЕТ ВОВА"), 200


