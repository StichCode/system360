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
    if not data:
        return jsonify(message="Bad args."), 400
    args = Checkout.from_dict(data)
    if not args:
        return jsonify(message="Checkout already exists"), 404
    return jsonify(message="Checkout has been create."), 200


@bp.route("/checkouts", methods=["DELETE"])
@jwt_required
def delete_checkout():
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = Checkout.delete_by_id(args)
    if d is not None:
        return jsonify(message=f"No checkout with this id"), 201
    return jsonify(message=f"Checkout has been delete."), 201