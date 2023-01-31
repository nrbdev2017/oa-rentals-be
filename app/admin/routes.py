from app.admin.http.admin_handler import get_admin_dashboard

from flask_restful import Resource, fields, marshal_with


class AdminAPI(Resource):
    """Definition for endpoints for the Admin Module"""

    @classmethod
    def get(cls):
        return get_admin_dashboard()
