from web_backend.database.models import Shops, Objects


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
