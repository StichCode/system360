import bcrypt

from web_backend.database.models import User, Role


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
    role = Role.query.filter_by(name=role).first()
    if role is None:
        return None
    users = User.query.filter_by(role=role.id).all()
    if users is None:
        return None
    return [user.to_dict() for user in users]
