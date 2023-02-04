from flask import Blueprint
# from app.admin.auth import auth_bp
from app.admin.permissions import permissions_bp
# from app.admin.roles import roles_bp
# from app.admin.users import users_bp

from flask_restful import Api

from app.admin.routes import AdminAPI

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# admin_bp.register_blueprint(auth_bp)
admin_bp.register_blueprint(permissions_bp)
# admin_bp.register_blueprint(roles_bp)
# admin_bp.register_blueprint(users_bp)

api = Api(admin_bp)
api.add_resource(AdminAPI, '/')

from app.admin import routes
