from flask import request, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, create_refresh_token

from web_backend.api import bp
from web_backend.api.errors import error_response
from web_backend.binder.user import verify_password


@bp.route("/test", methods=["GET"])
def test():
    return f"<h1>Hello World! </h1>"


@bp.route("/auth", methods=["POST"])
def login():
    data = request.get_json() or {}
    print(data)
    if not data:
        return jsonify(message="No data for authorization"), 402
    response = verify_password(data)
    if response is not None:
        response['access'] = create_access_token(identity=data["username"])
        response['refresh'] = create_refresh_token(identity=data["username"])
        return jsonify(response), 200
    return error_response(403)
