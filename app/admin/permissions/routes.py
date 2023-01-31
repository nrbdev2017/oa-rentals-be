from app.admin.permissions.controllers.permission_controller import register_permission, get_permissions, \
    update_permission, get_system_permissions

from flask_restful import Resource, fields, marshal_with

resource_fields = {
    'id': fields.String,
    'a_code': fields.String,
    'a_desc': fields.String,
    'perm_func': fields.String,
    'a_status': fields.String,
    'created_at': fields.String,
    'updated_at': fields.String,
    'updated_by': fields.String,
}


class PermissionsAPI(Resource):
    """Definition for endpoints for the Permissions SubModule"""

    @classmethod
    @marshal_with(resource_fields)
    def get(cls):
        return get_permissions()

    @classmethod
    def post(cls):
        return register_permission()

    @classmethod
    def put(cls):
        return update_permission()


class SystemPermissionsAPI(Resource):
    @classmethod
    def get(cls):
        return get_system_permissions()
