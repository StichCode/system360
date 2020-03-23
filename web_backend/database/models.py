from enum import Enum

from web_backend import db
from web_backend.database.base_models import BaseModel, BaseUser


class User(BaseUser, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)  # FIXME handle username uniqueness error
    email = db.Column(db.String(64), unique=True, nullable=False)  # FIXME handle email uniqueness error
    phone = db.Column(db.String(12), nullable=True, server_default='')  # FIXME handle phone uniqueness error
    password = db.Column(db.String(255), nullable=False)  # FIXME do unicode value

    first_name = db.Column(db.String(100), nullable=True, server_default='')
    last_name = db.Column(db.String(100), nullable=True, server_default='')

    role = db.Column(db.Integer, db.ForeignKey('roles.id'))

    franchise_id = db.Column(db.Integer, db.ForeignKey('franchises.id'))


class Role(BaseModel, db.Model):
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


class Shops(BaseModel, db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(12), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Objects(BaseModel, db.Model):
    __tablename__ = 'objects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), nullable=False)
    type = db.Column(db.String(64), nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)


class Franchise(BaseModel, db.Model):
    __tablename__ = 'franchises'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), unique=True, nullable=False)


class TypeCheckout(Enum):
    """
    regular - регулярные проверки
    extraordinary - внеочередные проверки
    """
    regular = "regular"
    extraordinary = "extraordinary"


class Checkouts(BaseModel, db.Model):
    __tablename__ = 'checkouts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)
    start = db.Column(db.DateTime, nullable=False, comment="время начала задачи")
    end = db.Column(db.DateTime, nullable=False, comment="время конца задачи")
    worker = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, comment="пользователь с ролью работник")
    type = db.Column(db.Enum(TypeCheckout), nullable=False, comment="Тип проверки")


class CheckoutTask(BaseModel, db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    object_id = db.Column(db.Integer, db.ForeignKey('objects.id'), nullable=False)
    checkout = db.Column(db.Integer, db.ForeignKey('checkouts.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, comment="статус задачи")
    title = db.Column(db.String(100), nullable=False, comment="название задачи")


class CheckoutSubTask(BaseModel, db.Model):
    __tablename__ = 'sub_tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    title = db.Column(db.String(256), nullable=False, comment="название подзадачи")