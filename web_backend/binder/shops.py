from web_backend import db
from web_backend.binder.users import get_user_by_id
from web_backend.database.models import Shop


def get_shops_by_user(user_id):
    result = []
    shops = Shop.query.filter_by(user_id=user_id).all()
    if shops is None:
        return []
    for shop in shops:
        result.append({
            "shopId": shop.id,
            "shopAddress": shop.address,
            "shopPhone": shop.phone,
            "userId": int(user_id),
        })
    return result


def new_shop(data):
    result = {}
    for field in ["address", "phone", "user_id"]:
        if field in data:
            result[field] = data[field]
    obj = Shop(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id


def shops_get():
    result = []
    for shop in Shop.query.all():
        result.append({
            "shopId": shop.id,
            "address": shop.address,
            "phone": shop.phone,
            "user": get_user_by_id(shop.user_id)
        })
    return result


def shop_delete(id_shop):
    Shop.query.filter(Shop.id == id_shop).delete(synchronize_session=False)
    db.session.commit()


def shop_by_id(shop_id):
    shop = Shop.query.filter(Shop.id == shop_id).first()
    return {
        "shopId": shop.id,
        "address": shop.address,
        "phone": shop.phone,
        "user": get_user_by_id(shop.user_id)
    }


def shop_by_user_id(user_id):
    shop = Shop.query.filter(Shop.user_id == user_id).first()
    return {
        "shopId": shop.id,
        "address": shop.address,
        "phone": shop.phone,
        "user": get_user_by_id(shop.user_id)
    }