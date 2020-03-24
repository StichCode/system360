import re

import bcrypt
from flask import jsonify, url_for
from sqlalchemy.exc import IntegrityError, InvalidRequestError, DataError

from web_backend.database.base_func import add_instance, delete_instance, edit_instance, get_all


class BaseModel(object):

    @classmethod
    def to_collection_dict(cls, page, per_page, endpoint, **kwargs):
        if kwargs:
            try:
                resources = cls.query.filter_by(**cls._prepare_dict(kwargs)).paginate(page, per_page, False)
            except (InvalidRequestError, DataError):
                return []
        else:
            resources = cls.query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data

    @classmethod
    def all_to_dict(cls):
        return [r.to_dict() for r in get_all(cls)]

    def to_dict(self):
        data = {}
        for attr, column in self.__mapper__.c.items():
            data[self._snake_to_camel(column.key)] = getattr(self, attr)
        return data

    def delete_by_id(self):
        delete_instance(self, self.id)

    @classmethod
    def from_dict(cls, data: dict, edit=False):
        result = {}
        data = cls._prepare_dict(data)
        keys = [column.key for _, column in cls.__mapper__.c.items()]
        for field in keys:
            if field == "id":
                continue
            elif field in data:
                result[field] = data[field]
        try:
            if not edit:
                add_instance(cls, **result)
            else:
                edit_instance(cls, data["id"], result)
        except IntegrityError:
            return False
        return True

    @classmethod
    def keys(cls):
        return [cls._snake_to_camel(column.key) for _, column in cls.__mapper__.c.items()]

    @classmethod
    def _prepare_dict(cls, data: dict) -> dict:
        new_dict = {}
        for k, v in data.items():
            new_dict[cls._camel_to_snake(k)] = v
        return new_dict

    @staticmethod
    def _snake_to_camel(s: str):
        if not re.findall("_", s):
            return s
        result = re.split("_", s)
        return result[0] + result[1].capitalize()

    @staticmethod
    def _camel_to_snake(s: str):
        camel = re.findall('([A-Z])', s)
        if not camel:
            return s
        camel = camel[0]
        result = re.split(camel, s)
        return result[0] + "_" + camel.lower() + result[1]


class BaseUser(BaseModel):

    @staticmethod
    def hash_pw(password: str):
        salt = bcrypt.gensalt(12)
        hashed = bcrypt.hashpw(password.encode("ascii"), salt)
        return hashed.decode("UTF-8")

    def to_dict(self):
        data = {}
        for attr, column in self.__mapper__.c.items():
            if column.key == "password":
                continue
            data[self._snake_to_camel(column.key)] = getattr(self, attr)
        return data

    @classmethod
    def from_dict(cls, data: dict, edit=False):
        result = {}
        data = cls._prepare_dict(data)
        keys = [column.key for _, column in cls.__mapper__.c.items()]
        for field in keys:
            if field in data:
                if field == "password":
                    result[field] = cls.hash_pw(data[field])
                else:
                    result[field] = data[field]
        try:
            if not edit:
                add_instance(cls, **result)
            else:
                edit_instance(cls, data["id"], result)
        except IntegrityError:
            return False
        return True