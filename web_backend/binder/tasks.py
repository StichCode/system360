from web_backend import db
from web_backend.binder.checkouts import checkout_by_id
from web_backend.binder.object import object_by_id
from web_backend.database.models import CheckoutTask


def tasks_get_all():
    result = []
    for task in CheckoutTask.query.all():
        result.append({
            "id": task.id,
            "object": object_by_id(task.object_id),
            "checkout": checkout_by_id(task.checkout),
            "status": task.status,
            "title": task.title
        })
    return result


def tasks_post(data):
    result = {}
    # FIXME сделать проверку на существование шопа и рабочего
    for field in ["object_id", "checkout", "status", "title"]:
        if field in data:
            result[field] = data[field]
    obj = CheckoutTask(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id


def tasks_delete(id_task):
    CheckoutTask.query.filter(CheckoutTask.id == id_task).delete(synchronize_session=False)
    db.session.commit()


def task_by_id(id_task):
    task = CheckoutTask.query.filter(CheckoutTask.id == id_task).first()
    return {
        "id": task.id,
        "object": object_by_id(task.object_id),
        "checkout": checkout_by_id(task.checkout),
        "status": task.status,
        "title": task.title
    }