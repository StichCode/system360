from web_backend import db
from web_backend.database.models import Franchise


def franchises_get():
    fr = Franchise.query.all()
    prepared_franchise = []
    for f in fr:
        prepared_franchise.append({
            "id": f.id,
            "title": f.title
        })
    return prepared_franchise


def franchises_post(data):
    new_fr = Franchise(**data)
    db.session.add(new_fr)
    db.session.commit()
    return new_fr.id


def my_franchises_delete(franchise_id):
    Franchise.query.filter(Franchise.id == franchise_id).delete(synchronize_session=False)
    db.session.commit()


def franchise_by_id(franchise_id):
    franchise = Franchise.query.filter(Franchise.id == franchise_id).first()
    return {
        "id": franchise.id,
        "title":franchise.title
    }
