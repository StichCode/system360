from flask import jsonify, request

from web_backend.api import bp
from web_backend.database.models import Shop


@bp.route("/shops", methods=["GET"])
# @jwt_required
def all_shops():
    shop = request.args.to_dict()
    q = None
    if not shop:
        return jsonify(Shop.all_to_dict()), 200
    if "id" in shop:
        q = Shop.query.filter_by(id=shop["id"]).first()
    elif "userId" in shop:
        q = Shop.query.filter_by(user_id=shop["userId"]).first()
    if q is not None:
        return jsonify(shop.to_dict()), 200
    return jsonify(message="No shops in database."), 400


@bp.route("/shops", methods=["POST"])
# @jwt_required
def create_shop():
    data = request.get_json() or {}
    if "address" not in data:
        pass
    shop = Shop.from_dict(data)
    if not shop:
        return jsonify(message="Shop already exists"), 403
    return jsonify(message="New shop has been created."), 201


@bp.route("/shops", methods=["DELETE"])
# @jwt_required
def delete_shop():
    shop = request.args.get("id", type=int)
    if shop is None:
        pass
    q = Shop.query.filter(Shop.id == shop).first()
    if q is not None:
        q.delete_by_id()
        return jsonify(message=f"Shop {q.id} has been delete."), 201
    return jsonify(message=f"No shop with this id"), 201


@bp.route("/shops", methods=["PUT"])
# @jwt_required
def get_shops():
    data = request.get_json() or {}
    if "id" not in data:
        return jsonify("Bad args"), 404
    shop = Shop.query.filter_by(id=data["id"]).first()
    if not shop:
        return jsonify(message="No shop with this id in database"), 201
    shop = shop.from_dict(data, True)
    if not shop:
        return jsonify(message="Shop can't be edit"), 401
    return jsonify(Shop.query.filter_by(id=data["id"]).first().to_dict()), 201
