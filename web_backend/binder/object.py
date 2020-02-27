from web_backend import db
from web_backend.database.models import Objects, Franchise, User, Shops


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


def object_get():
    objects = Objects.query.all()
    prepared_objects = []
    # FIXME переделать на join
    for obj in objects:
        shop = Shops.query.filter(Shops.id == obj.shop_id).first()
        user = User.query.filter(User.id == shop.user_id).first()
        franchise = Franchise.query.filter(Franchise.id == user.franchise_id).first()
        prepared_objects.append({
            "id": obj.id,
            "title": obj.title,
            "type": obj.type,
            "x": obj.x,
            "y": obj.y,
            "shop": {
                "shopId": shop.id,
                "address": shop.address,
                "phone": shop.phone,
                "user": {
                    "userId": user.id,
                    "username": user.username,
                    "email": user.email,
                    "phone": user.phone,
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "role": user.role,
                    "franchise": {
                        "franchiseId": franchise.id,
                        "franchiseName": franchise.title
                    }
                }
            },

        })
    return prepared_objects


def object_delete(obj_id):
    Objects.query.filter(Objects.id == obj_id).franchises_delete(synchronize_session=False)
    db.session.commit()


def object_post(data):
    result = {}
    for field in ["title", "type", "x", "y", "shop_id"]:
        if field in data:
            result[field] = data[field]
    obj = Objects(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id
