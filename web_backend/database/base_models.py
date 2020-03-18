import re

from sqlalchemy.exc import IntegrityError

from web_backend.database.base_func import add_instance


class BaseModel(object):

    def to_dict(self):
        data = {}
        for attr, column in self.__mapper__.c.items():
            if column.key == "password":
                continue
            data[self.snake_to_camel(column.key)] = getattr(self, attr)
        return data

    @classmethod
    def from_dict(cls, data: dict):
        result = {}
        data = cls.prepare_dict(data)
        keys = [column.key for _, column in cls.__mapper__.c.items()]
        for field in keys:
            if field in data:
                result[field] = data[field]
        try:
            add_instance(cls, **result)
        except IntegrityError:
            pass

    @classmethod
    def keys(cls):
        return [cls.snake_to_camel(column.key) for _, column in cls.__mapper__.c.items()]

    @classmethod
    def prepare_dict(cls, data: dict) -> dict:
        new_dict = {}
        for k, v in data.items():
            new_dict[cls.camel_to_snake(k)] = v
        return new_dict

    @staticmethod
    def snake_to_camel(s: str):
        if not re.findall("_", s):
            return s
        result = re.split("_", s)
        return result[0] + result[1].capitalize()

    @staticmethod
    def camel_to_snake(s: str):
        camel = re.findall('([A-Z])', s)
        if not camel:
            return s
        camel = camel[0]
        result = re.split(camel, s)
        return result[0] + "_" + camel.lower() + result[1]


class BaseUser(BaseModel):

    @classmethod
    def from_dict(cls, data=None):
        pass


class BaseShops(BaseModel):

    @classmethod
    def from_dict(cls, data=None):
        pass


class BaseObjects(BaseModel):

    @classmethod
    def from_dict(cls, data=None):
        pass


class BaseCheckouts(BaseModel):

    @classmethod
    def from_dict(cls, data=None):
        pass


class BaseCheckoutTask(BaseModel):

    @classmethod
    def from_dict(cls, data=None):
        pass
