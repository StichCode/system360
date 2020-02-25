import random

import bcrypt

from web_backend.database.models import User, Role


def hash_pw(password: str):
    salt = bcrypt.gensalt(random.randint(15, 31))
    hashed = bcrypt.hashpw(password.encode("ascii"), salt)
    return hashed.decode("UTF-8")


def verify_password(data):
    user = User.query.filter_by(username=data["username"]).first()
    if user is None:
        return None
    role = Role.query.filter_by(id=user.role).first()
    if role is None:
        return None
    response = {
        "userId": user.id,
        "role": role.name,
        }
    if user:
        if bcrypt.checkpw(data["password"].encode("ascii"),
                          user.password_hash.encode("ascii")):
            return response
    return None


def users_by_role(role):
    all_users = []
    role = Role.query.filter_by(name=role).first()
    if role is None:
        return all_users
    users = User.query.filter_by(role=role.id).all()
    if users is None:
        return all_users
    for user in users:
        all_users.append({
            "userId": user.id,
            "userName": user.username,
            "role": role.name,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "userPhone": user.phone
        })
    return all_users


def new_user(data):
    role = Role.query.filter_by(name=data["role"]).first()

    result = {}
    for field in ["username", "email", "phone", "password", "first_name", "last_name", "role", "franchise_id"]:
        if field in data:
            result[field] = data["field"]
        if field == "password":
            result[field] = hash_pw(data["password"])
        if field == "role":
            result["field"] = role.id
    return User(**result)
