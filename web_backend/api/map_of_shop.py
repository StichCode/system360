from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.binder.object import get_map_of_shop, object_delete, object_post


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
