from web_backend import db
# from web_backend.binder.shops import shop_by_id
from web_backend.database.models import Object


def get_map_of_shop(shop_id):
    result = []
    map_shop = Object.query.filter_by(shop_id=shop_id).all()
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


def object_get():
    objects = Object.query.all()
    prepared_objects = []
    # FIXME переделать на join
    for obj in objects:
        prepared_objects.append({
            "id": obj.id,
            "title": obj.title,
            "type": obj.type,
            "x": obj.x,
            "y": obj.y,
            # "shop": shop_by_id(obj.shop_id),

        })
    return prepared_objects


def object_delete(obj_id):
    Object.query.filter(Object.id == obj_id).myfranchises_delete(synchronize_session=False)
    db.session.commit()


def object_post(data):
    result = {}
    for field in ["title", "type", "x", "y", "shop_id"]:
        if field in data:
            result[field] = data[field]
    obj = Object(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id


def object_by_id(object_id):
    obj = Object.query.filter(Object.id == object_id).first()
    return {
            "id": obj.id,
            "title": obj.title,
            "type": obj.type,
            "x": obj.x,
            "y": obj.y,
            # "shop": shop_by_id(obj.shop_id)
            }