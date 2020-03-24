from flask import jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.database.models import Checkout


@bp.route("/checkouts", methods=["GET"])
@jwt_required
def checkout():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = Checkout.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


@bp.route("/checkouts", methods=["POST"])
@jwt_required
def new_checkout():
    data = request.get_json() or {}

    if not data or "shop_id" not in data \
            or "start" not in data\
            or "end" not in data\
            or "worker" not in data\
            or "type" not in data:
        return jsonify(message="Bad parameters"), 401
    response = ...
    if isinstance(response, str):
        return jsonify(message=response), 403
    return jsonify(message="checkout has been created"), 201


@bp.route("/checkouts", methods=["DELETE"])
@jwt_required
def delete_checkout():
    try:
        checkouts_id = int(request.args["id"])
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    return jsonify(message="Franchise hs been delete"), 201