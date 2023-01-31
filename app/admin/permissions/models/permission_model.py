import uuid
from datetime import datetime

from .permission import Permission
from app import db


class PermissionModel:

    @classmethod
    def get_permissions(cls):
        return Permission.query.all()

    @classmethod
    def get_system_permissions(cls):
        return Permission.query.all()

    @classmethod
    def get_permission_by_id(cls, perm_id):
        return Permission.query.filter_by(id=perm_id).one_or_none()

    @classmethod
    def get_permission_by_code(cls, perm_code):
        return Permission.query.filter_by(perm_code=perm_code).one_or_none()

    @classmethod
    def get_permission_by_name(cls, perm_name):
        return Permission.query.filter_by(perm_name=perm_name).one_or_none()

    @classmethod
    def get_permission_for_function(cls, function_name):
        return Permission.query.filter_by(function_name=function_name).one_or_none()

    @classmethod
    def get_module_permissions(cls):
        return __name__

    @classmethod
    def register_permission(cls, permission):
        try:
            exists = False
            for perm_dict in get_all_functions():
                if perm_dict['qualified_function'] == permission['qualified_function']:
                    exists = True
                    break

            if exists:
                to_save = Permission(
                    id=str(uuid.uuid4()),
                    a_code=permission['a_code'],
                    a_desc=permission['a_desc'],
                    qualified_function=permission['qualified_function'],
                    a_status=permission['a_status'],
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow()
                )
                return "Save works"
            else:
                return "Exception Raised"
                # raise Exception("Not a Valid Permission")
        except Exception as e:
            print('*****' + __name__ + ' register_permission error****')
            print(str(e))
            raise Exception(e)

    @classmethod
    def update_permission(cls):
        return __name__

    @classmethod
    def delete_permission(cls):
        return __name__
