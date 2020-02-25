from web_backend import db
from web_backend.database.models import Objects


def get_map_of_shop(shop_id):
    result = []
    map_shop = Objects.query.filter_by(shop_id=shop_id).all()
    if map_shop is None:
        return []
    for obj in map_shop:
        result.append({
            "mapObjectId": obj.id,
            "title": obj.title,
            "type": obj.type,
            "x": obj.x,
            "y": obj.y,
        })
    return result


def object_delete(obj_id):
    Objects.query.filter(Objects.id == obj_id).delete(synchronize_session=False)
    db.session.commit()


def new_object(data):
    result = {}
    for field in ["title", "type", "x", "y", "shop_id"]:
        if field in data:
            result[field] = data[field]
    obj = Objects(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id

