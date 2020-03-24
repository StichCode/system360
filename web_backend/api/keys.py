from flask import jsonify
from flask_jwt_extended import jwt_required

from web_backend.api import bp
from web_backend.database.models import Role, User, Shop, Object, Franchise, CheckoutSubTask, CheckoutTask, Checkout


@bp.route("/keys/role", methods=["GET"])
@jwt_required
def keys_role():
    return jsonify(Role.keys())


@bp.route("/keys/user", methods=["GET"])
@jwt_required
def keys_user():
    return jsonify(User.keys())


@bp.route("/keys/shop", methods=["GET"])
@jwt_required
def keys_shop():
    return jsonify(Shop.keys())


@bp.route("/keys/object", methods=["GET"])
@jwt_required
def keys_object():
    return jsonify(Object.keys())


@bp.route("/keys/franchise", methods=["GET"])
@jwt_required
def keys_franchise():
    return jsonify(Franchise.keys())


@bp.route("/keys/checkout", methods=["GET"])
@jwt_required
def keys_checkout():
    return jsonify(Checkout.keys())


@bp.route("/keys/checkout_task", methods=["GET"])
@jwt_required
def keys_checkout_task():
    return jsonify(CheckoutTask.keys())


@bp.route("/keys/checkout_sub_task", methods=["GET"])
@jwt_required
def keys_checkout_sub_task():
    return jsonify(CheckoutSubTask.keys())