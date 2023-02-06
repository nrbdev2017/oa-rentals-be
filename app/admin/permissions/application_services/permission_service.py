from app.admin.permissions.infrastructure.repos.sa_permission_repository import SAPermissionRepository
from ..domain.entities.permission import Permission  
from ..domain.entities.value_objects.permission_id import PermissionId  

class PermissionService:
    """Handles permission related functions"""
    perm_repo: SAPermissionRepository

    def __init__(self):
        self.perm_repo = SAPermissionRepository()

    def get_all_permissions(self):
        return self.perm_repo.get_all()

    def register_permission(self, data):
        permission = Permission (
            PermissionId(),
            data['a_name'],
            data['a_code'],
            data['a_desc'],
            data['qualified_function'],
            data['a_status']
        )
        return self.perm_repo.add(permission)
