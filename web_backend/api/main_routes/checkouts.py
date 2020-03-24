from flask import jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp


@bp.route("/checkouts", methods=["GET"])
@jwt_required
def checkout():
    checkouts = ...
    print(checkouts)
    if checkouts:
        return jsonify(checkouts), 200
    return jsonify(message="No franchises in database."), 400


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