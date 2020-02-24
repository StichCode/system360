from web_backend import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)  # FIXME handle username uniqueness error
    email = db.Column(db.String(64), unique=True, nullable=False)  # FIXME handle email uniqueness error
    phone = db.Column(db.String(12))  # FIXME handle phone uniqueness error
    password_hash = db.Column(db.String(255), nullable=False)  # FIXME do unicode value

    first_name = db.Column(db.String(100), nullable=False, server_default='')
    last_name = db.Column(db.String(100), nullable=False, server_default='')

    role = db.Column(db.Integer, db.ForeignKey('roles.id'))


class Role(db.Model):
    """
    Owner
    Manager
    Auditor
    Ordinary worker
    Administrator
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), index=True, unique=True)

# Now need 1 to 1
# class UserRoles(db.Model):
#     __tablename__ = 'user_roles'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))
