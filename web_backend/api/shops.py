from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.binder.shops import get_shops_by_user, new_shop


@bp.route("/shops", methods=["GET"])
@jwt_required
def get_shops():
    try:
        user_id = request.args["userId"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    print(user_id)
    shops = get_shops_by_user(user_id)
    if shops:
        return jsonify(shops), 201
    return jsonify(status=400, message="No shops with for this user.")


@bp.route("/new_shop", methods=["POST"])
@jwt_required
def create_shop():

    data = request.get_json() or {}
    if not data:
        return jsonify(message="Bad parameters"), 401

    new = new_shop(data)

    if new:
        return jsonify(shop_id=new, message="Shop has be created"), 201
    return jsonify(status=400, message="No shops with for this user.")
