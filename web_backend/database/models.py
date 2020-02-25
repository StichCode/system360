from web_backend import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)  # FIXME handle username uniqueness error
    email = db.Column(db.String(64), unique=True, nullable=False)  # FIXME handle email uniqueness error
    phone = db.Column(db.String(12), nullable=True, server_default='')  # FIXME handle phone uniqueness error
    password_hash = db.Column(db.String(255), nullable=False)  # FIXME do unicode value

    first_name = db.Column(db.String(100), nullable=True, server_default='')
    last_name = db.Column(db.String(100), nullable=True, server_default='')

    role = db.Column(db.Integer, db.ForeignKey('roles.id'))

    franchise_id = db.Column(db.Integer, db.ForeignKey('franchises.id'))


class Role(db.Model):
    """
    owner
    manager
    auditor
    worker
    admin
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), index=True, unique=True)


class Shops(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(12), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Objects(db.Model):
    __tablename__ = 'objects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), nullable=False)
    type = db.Column(db.String(64), nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)


class Franchise(db.Model):
    __tablename__ = 'franchises'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), nullable=False)
