from web_backend import db
from web_backend.database.models import Checkouts, Shops, User


def checkouts_get_all():
    result = []
    for checkout in Checkouts.query.all():
        checkout: Checkouts
        shop = Shops.query.filter(Shops.id == checkout.shop_id).first()
        user = User.query.filter(User.id == shop.user_id).first()
        franchise = User
        worker = User.query.filter(User.id == checkout.worker).first()
        result.append({
            "id": checkout.id,
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
                },
            },
            "start": checkout.start,
            "end": checkout.end,
            "user": {
                    "userId": worker.id,
                    "username": worker.username,
                    "email": worker.email,
                    "phone": worker.phone,
                    "firstName": worker.first_name,
                    "lastName": worker.last_name,
                    "role": worker.role,
                    "franchise": {
                        "franchiseId": franchise.id,
                        "franchiseName": franchise.title
                    }
                },
            "type": checkout.type

        })
    return result


def checkouts_post(data):
    result = {}
    # FIXME сделать проверку на существование шопа и рабочего
    for field in ["shop_id", "start", "end", "worker", "type"]:
        if field in data:
            result[field] = data[field]
    obj = Checkouts(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id


def checkouts_delete(id_checkout):
    Checkouts.query.filter(Checkouts.id == id_checkout).delete(synchronize_session=False)
    db.session.commit()