from datetime import datetime

from web_backend import db
from web_backend.binder.shops import shop_by_id
from web_backend.binder.users import get_user_by_id
from web_backend.database.models import Checkouts


def checkouts_get_all():
    result = []
    for checkout in Checkouts.query.all():
        result.append({
            "id": checkout.id,
            "shop": shop_by_id(checkout.shop_id),
            "start": checkout.start.strftime("%d-%m-%Y %H:%M:%S"),
            "end": checkout.end.strftime("%d-%m-%Y %H:%M:%S"),
            "user": get_user_by_id(checkout.worker),
            "type": checkout.type.value
        })
    return result


def checkouts_post(data):
    result = {}
    # FIXME сделать проверку на существование шопа и рабочего
    for field in ["shop_id", "start", "end", "worker", "type"]:
        if field in data:
            if field == "start" or field == "end":
                result[field] = datetime.strptime(data[field], "%d-%m-%Y %H:%M:%S")
                continue
            result[field] = data[field]
    obj = Checkouts(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id


def checkouts_delete(id_checkout):
    Checkouts.query.filter(Checkouts.id == id_checkout).delete(synchronize_session=False)
    db.session.commit()


def checkout_by_id(checkout_id):
    checkout = Checkouts.query.filter(Checkouts.id == checkout_id).firast()
    return {
        "id": checkout.id,
        "shop": shop_by_id(checkout.shop_id),
        "start": checkout.start.strftime("%d-%m-%Y %H:%M:%S"),
        "end": checkout.end.strftime("%d-%m-%Y %H:%M:%S"),
        "user": get_user_by_id(checkout.worker),
        "type": checkout.type.value
    }