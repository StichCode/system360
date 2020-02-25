from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.binder.shop_objects import get_map_of_shop, object_delete, new_object


@bp.route("/map", methods=["GET"])
@jwt_required
def get_map():
    try:
        shop_id = request.args["shopId"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    map_shop = get_map_of_shop(shop_id)
    if map_shop:
        return jsonify(map_shop), 201
    return jsonify(message="No map for this shop."), 400


@bp.route("/del_object", methods=["POST"])
@jwt_required
def del_object():
    try:
        obj_id = request.args["objectID"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    object_delete(obj_id)
    return jsonify(message=f"Object {obj_id} has been deleted"), 201


@bp.route("/edit_object", methods=["PUT"])
@jwt_required
def change_object():
    pass


@bp.route("/create_object", methods=["POST"])
@jwt_required
def create_object():
    data = request.get_json() or {}
    print(data)
    if not data:
        jsonify(message="Bad data"), 401
    obj = new_object(data)
    return


