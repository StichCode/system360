from web_backend import db
from web_backend.database.models import Shops


def get_shops_by_user(user_id):
    result = []
    shops = Shops.query.filter_by(user_id=user_id).all()
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
    obj = Shops(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id
