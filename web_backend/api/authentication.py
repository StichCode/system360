from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from web_backend.api import bp
from web_backend.api.errors import error_response
from web_backend.binder.methods_user import verify_password, users_by_role


@bp.route("/test", methods=["GET"])
def test():
    return f"<h1>Hello World! </h1>"


@bp.route("/auth", methods=["POST"])
def login():
    data = request.get_json() or {}
    response = verify_password(data)
    if response is not None:
        response['access_token'] = create_access_token(identity=data["username"])
        response['refresh_token'] = create_refresh_token(identity=data["username"])
        return jsonify(response), 200
    return error_response(403)


@bp.route("/users", methods=["GET"])
@jwt_required
def get_users_by_role():
    current_user = get_jwt_identity()
    role_id = request.args["roleId"]
    print(role_id)
    users = users_by_role(role_id)
    if users:
        return jsonify(users)
    return jsonify(status=400, message="No users with this roles.")


