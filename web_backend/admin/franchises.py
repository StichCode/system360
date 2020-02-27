from flask import jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.admin import bp
from web_backend.binder.franchises import franchises_get, franchises_post, franchises_delete


@bp.route("/franchises", methods=["GET"])
@jwt_required
def franchise():
    franchises = franchises_get()
    if franchises:
        return jsonify(franchises), 201
    return jsonify(status=400, message="No franchises in database.")


@bp.route("/franchises", methods=["POST"])
@jwt_required
def new_franchise():
    data = request.get_json() or {}
    if not data or "title" not in data:
        return jsonify(message="Bad parameters"), 401
    return jsonify(franchises_post(data)), 201


@bp.route("/franchises", methods=["DELETE"])
@jwt_required
def delete_franchise():
    try:
        franchise_id = int(request.args["id"])
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    franchises_delete(franchise_id)
    return jsonify(message="Franchise hs been delete"), 201