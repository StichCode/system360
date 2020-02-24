from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

from web_backend.api import bp
from web_backend.api.errors import error_response
from web_backend.binder.methods_user import verify_password


@bp.route("/test", methods=["GET"])
def test():
    return f"<h1>Hello World! </h1>"


@bp.route("/auth", methods=["POST"])
def login():
    data = request.get_json() or {}
    if not data:
        return jsonify(message="No data for authorization"), 403
    response = verify_password(data)
    if response is not None:
        response['access_token'] = create_access_token(identity=data["username"])
        response['refresh_token'] = create_refresh_token(identity=data["username"])
        return jsonify(response), 200
    return error_response(403)
