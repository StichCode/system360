import bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

from web_backend.api import bp
from web_backend.database.models import User, Role


@bp.route("/auth", methods=["POST"])
def login():
    data = request.get_json() or {}
    if not data or "username" not in data or "password" not in data:
        return jsonify(message="No data for authorization"), 402
    response = verify_password(data)
    if response is not None:
        response['access'] = create_access_token(identity=data["username"])
        response['refresh'] = create_refresh_token(identity=data["username"])
        return jsonify(response), 200
    return jsonify(message="User does't created"), 403


def verify_password(data):
    user = User.query.filter_by(username=data["username"]).first()
    if user is None:
        return None
    role = Role.query.filter_by(id=user.role).first()
    if role is None:
        return None
    if user:
        if bcrypt.checkpw(data["password"].encode("ascii"),
                          user.password.encode("ascii")):
            return {"userId": user.id, "role": role.name}
    return None