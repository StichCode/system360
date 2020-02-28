from web_backend import db
from web_backend.binder.tasks import task_by_id
from web_backend.database.models import CheckoutSubTask


def subtasks_get_all():
    result = []
    for subtask in CheckoutSubTask.query.all():
        result.append({
            "id": subtask.id,
            "task": task_by_id(subtask.task),
            "title": subtask.title,
        })
    return result


def subtasks_post(data):
    result = {}
    # FIXME сделать проверку на существование шопа и рабочего
    for field in ["task", "title"]:
        if field in data:
            result[field] = data[field]
    obj = CheckoutSubTask(**result)
    db.session.add(obj)
    db.session.commit()
    return obj.id


def subtasks_delete(id_subtask):
    CheckoutSubTask.query.filter(CheckoutSubTask.id == id_subtask).delete(synchronize_session=False)
    db.session.commit()