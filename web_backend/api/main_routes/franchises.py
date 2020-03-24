from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.database.models import Franchise


@bp.route("/franchises", methods=["GET"])
# @jwt_required
def get_franchise_by():
    args = request.args.to_dict()
    return Franchise.middle_get(args)


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
    franchise = request.args.get("id", type=int)
    if franchise is None:
        return jsonify(message="Bad id for delete"), 400
    franchise = Franchise.query.filter_by(id=franchise).first()
    if franchise is not None:
        franchise.delete_by_id()
        return jsonify(message=f"Franchise {franchise} has been delete"), 201
    return jsonify(message="No franchise with this id"), 400


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