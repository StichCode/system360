from flask import jsonify, request
from flask_jwt_extended import jwt_required

from web_backend.admin import bp
from web_backend.binder.shops import new_shop, shops_get


@bp.route("/shops", methods=["GET"])
# @jwt_required
def all_shops():
    shops = shops_get()
    if shops:
        return jsonify(shops), 201
    return jsonify(status=400, message="No shops in database.")


@bp.route("/shops", methods=["POST"])
@jwt_required
def create_shop():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="Bad parameters"), 401
    new = new_shop(data)
    if new:
        return jsonify(shop_id=new, message="Shop has be created"), 201
    return jsonify(status=400, message="No shops with for this user.")