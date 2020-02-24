from flask import jsonify
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_refresh_token_required

from web_backend import jwt
from web_backend.api import bp


@bp.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
def refresh():
    username = get_jwt_identity()
    response = {
        "access_token": create_access_token(identity=username)
    }
    return jsonify(access_token=response)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'userId': user.id, 'roles': user.role}
