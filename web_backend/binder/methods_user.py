import random

import bcrypt

from web_backend import auth
from web_backend.database.models import User, Role


@auth.hash_password
def hash_pw(password: str):
    salt = bcrypt.gensalt(random.randint(15, 31))
    hashed = bcrypt.hashpw(password.encode("ascii"), salt)
    return hashed.decode("UTF-8")


@auth.verify_password
def verify_password(uname: str, password: str):
    user = User.query.filter_by(username=uname).first()
    if user is not None:
        if bcrypt.checkpw(password.encode("ascii"),
                          user.password_hash.encode("ascii")):
            return True
    return False


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
