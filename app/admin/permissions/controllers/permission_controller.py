from app.admin.permissions.models.permission_model import PermissionModel
from flask import request

# from app.core.util.get_all_functions import get_all_functions


def get_permissions():
    return PermissionModel.get_permissions()


def get_system_permissions():
    return 'get_all_functions()'


def get_permission_by_id():
    return __name__


def get_permission_by_code():
    return __name__


def get_permission_by_name():
    return __name__


def get_module_permissions():
    return __name__


def register_permission():
    post_data = request.get_json()
    return PermissionModel.register_permission(post_data)


def update_permission():
    return __name__


def delete_permission():
    return __name__
