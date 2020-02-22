import random

import bcrypt

from web_backend import auth
from web_backend.database.models import User, Role


@auth.hash_password
def hash_pw(password: str):
    salt = bcrypt.gensalt(random.randint(15, 31))
    hashed = bcrypt.hashpw(password.encode("ascii"), salt)
    return hashed.decode("UTF-8")


def verify_password(data):
    user = User.query.filter_by(username=data["username"]).first()
    if user is None:
        return None
    role = Role.query.filter_by(id=user.role).first()
    response = {
        "userId": user.id,
        "role": role.name,
        "access": "access",
        "refresh": "refresh"}
    if user:
        if bcrypt.checkpw(data["password"].encode("ascii"),
                          user.password_hash.encode("ascii")):
            return response
    return None


def users_by_role(role):
    all_users = []
    role_id = Role.query.filter_by(name=role).first()
    if role_id is None:
        return all_users
    users = User.query.filter_by(role=role_id.id).all()
    if users is None:
        return all_users
    for user in users:
        all_users.append({
            "userId": user.id,
            "userName": user.username,
            "roleId": role,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "userPhone": user.phone
        })
    return all_users
