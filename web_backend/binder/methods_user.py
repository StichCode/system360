import random

import bcrypt

from web_backend import auth
from web_backend.database.models import User


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


def users_by_role():
    all_users = []
    users = User
