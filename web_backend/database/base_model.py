import re


class BaseModel(object):

    def to_dict(self):
        data = {}
        for attr, column in self.__mapper__.c.items():
            if column.key == "password":
                continue
            data[self.snake_to_camel(column.key)] = getattr(self, attr)
        return data

    @classmethod
    def from_dict(cls, data):
        result = {}
        print(cls)
        # keys = [column.key for _, column in cls.__mapper__.c.items()]
        # for field in keys:
        #     if field in data:
        #         result[field] = data[field]
        # return cls(**result)


    @staticmethod
    def snake_to_camel(s: str):
        if not re.findall("_", s):
            return s
        result = re.split("_", s)
        return result[0]+result[1].capitalize()

    @staticmethod
    def camel_to_snake(s: str):
        camel = re.findall('([A-Z])', s)
        if not camel:
            return s
        camel = camel[0]
        result = re.split(camel, s)
        return result[0] + "_" + camel.lower() + result[1]