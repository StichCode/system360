from functools import wraps
from flask_login import current_user


def role_required(role_name):
    def wrapper(view_function):
        @wraps(view_function)
        def decorator(*args, **kwargs):
            # if not current_user.has_role

            return view_function(*args, **kwargs)


    pass
