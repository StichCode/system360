from web_backend.database.models import Role


def role_by_id(role_id):
    role = Role.query.filter(Role.id == role_id).first()
    return {
        "id": role.id,
        "name": role.name
    }