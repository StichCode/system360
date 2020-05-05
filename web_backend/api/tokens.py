from flask import jsonify
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_refresh_token_required

from web_backend import jwt
from web_backend.api import bp


@bp.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
def refresh():
    username = get_jwt_identity()
    response = {
        "access": create_access_token(identity=username)
    }
    return jsonify(response)


@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    return jsonify({
        'msg': 'The {} token has expired'.format(token_type)
    }), 405