import bcrypt

from web_backend import db
from web_backend.binder.franchises import franchise_by_id
from web_backend.binder.roles import role_by_id
from web_backend.database.models import User, Role


def hash_pw(password: str):
    salt = bcrypt.gensalt(12)
    hashed = bcrypt.hashpw(password.encode("ascii"), salt)
    return hashed.decode("UTF-8")


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
            "role": role_by_id(user.role),
            "firstName": user.first_name,
            "lastName": user.last_name,
            "userPhone": user.phone
        })
    return all_users


def user_post(data):
    role = Role.query.filter_by(name=data["role"]).first()
    result = {}
    for field in ["username", "email", "phone", "password", "first_name", "last_name", "role", "franchise_id"]:
        if field in data:
            result[field] = data[field]
            continue
        if field == "password":
            result[field] = hash_pw(data["password"])
            continue
        if field == "role":
            result[field] = int(role.id)
            continue
    return User(**result)


def user_get():
    result = []
    for user in User.query.all():
        result.append({
            "userId": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "role": user.role,
            "franchise": franchise_by_id(user.franchise_id)
        })
    return result


def user_delete(user_id):
    User.query.filter(User.id == user_id).delete(synchronize_session=False)
    db.session.commit()


def get_user_by_id(user_id):
    user = User.query.filter(User.id == user_id).first()
    role = role_by_id(user.role)
    result = {
            "userId": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "role": role,
            "franchise": franchise_by_id(user.franchise_id)
        }
    return result