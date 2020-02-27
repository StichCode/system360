from flask import request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequestKeyError

from web_backend.api import bp
from web_backend.binder.shops import get_shops_by_user


@bp.route("/shops", methods=["GET"])
@jwt_required
def get_shops():
    try:
        user_id = request.args["userId"]
    except BadRequestKeyError:
        return jsonify(message="Bad parameters"), 401
    print(user_id)
    shops = get_shops_by_user(user_id)
    if shops:
        return jsonify(shops), 201
    return jsonify(status=400, message="No shops with for this user.")