from flask import Blueprint
from flask_restful import Api

from app.admin.permissions.routes import PermissionsAPI, SystemPermissionsAPI

permissions_bp = Blueprint('permissions', __name__, url_prefix='/permissions')
api = Api(permissions_bp)

api.add_resource(PermissionsAPI, '/')
# api.add_resource(SystemPermissionsAPI, '/system')

from app.admin.permissions import routes
