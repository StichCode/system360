from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.database.models import Franchise


@bp.route("/franchises", methods=["GET"])
# @jwt_required
def get_franchise_by():
    args = request.args.to_dict()
    page = int(args.pop('page', 1))
    per_page = int(args.pop('per_page', 10))
    data = Franchise.to_collection_dict(page, per_page, request.endpoint, **args)
    if not data:
        return jsonify(message="No data with this criteria."), 400
    return jsonify(data), 200


@bp.route("/franchises", methods=["POST"])
@jwt_required
def create_new_franchise():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="No data for create franchise"), 400
    franchise = Franchise.from_dict(data)
    if not franchise:
        return jsonify(message="Franchise already exists"), 404
    return jsonify(Franchise.query.filter_by(title=data["title"]).first().to_dict()), 200


@bp.route("/franchises", methods=["DELETE"])
@jwt_required
def delete_franchise():
    args = request.args.get("id", type=int)
    if args is None:
        return jsonify(message="Bad args."), 200
    d = Franchise.delete_by_id(args)
    if d is not None:
        return jsonify(message=f"No franchise with this id"), 201
    return jsonify(message=f"Franchise has been delete."), 201


@bp.route("/franchises", methods=["PUT"])
@jwt_required
def edit_franchise():
    try:
        data = request.get_json() or {}
    except BadRequestKeyError:
        return jsonify(message="No data for edit"), 400
    franchise = Franchise.query.get_or_404(data["id"])
    franchise = franchise.from_dict(data, True)
    if not franchise:
        return jsonify(message="Franchise can't be edit"), 401
    return jsonify(Franchise.query.filter_by(id=data["id"]).first().to_dict()), 201


def get_all_franchises():
    franchises = [role.to_dict() for role in Franchise.query.all()]
    if not franchises:
        return jsonify(message="No franchises in database"), 400
    return jsonify(franchises), 200