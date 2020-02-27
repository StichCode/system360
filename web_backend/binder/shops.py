from web_backend import db
from web_backend.database.models import Shops, User, Franchise


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


def shops_get():
    result = []
    for shop in Shops.query.all():
        user = User.query.filter(User.id == shop.user_id).first()
        franchise = Franchise.query.filter(Franchise.id == user.franchise_id).first()
        result.append({
            "shopId": shop.id,
            "address": shop.address,
            "phone": shop.phone,
            "user": {
                "userId": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
                "firstName": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "franchise": {
                    "franchiseId": franchise.id,
                    "franchiseName": franchise.title
                }
            }
        })
    return result


def shop_delete(id_shop):
    Shops.query.filter(Shops.id == id_shop).delete(synchronize_session=False)