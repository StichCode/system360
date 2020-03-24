from flask import jsonify, request
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import Shop


@bp.route("/shops", methods=["GET"])
@jwt_required
def all_shops():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = Shop.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


@bp.route("/shops", methods=["POST"])
@jwt_required
def create_shop():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="Bad args."), 400
    args = Shop.from_dict(data)
    if not args:
        return jsonify(message="Shop already exists"), 404
    return jsonify(message="Shop has been create."), 200


@bp.route("/shops", methods=["DELETE"])
@jwt_required
def delete_shop():
    shop = request.args.get("id", type=int)
    if shop is None:
        return jsonify(message="Bad args."), 200
    d = Shop.delete_by_id(shop)
    if not d:
        return jsonify(message=f"No shop with this id"), 201
    return jsonify(message=f"Shop has been delete."), 201


@bp.route("/shops", methods=["PUT"])
@jwt_required
def edit_shop():
    data = request.get_json() or {}
    if not data or data.get("id") is None:
        return jsonify(message="Bad args."), 400
    return Shop.global_edit(data)