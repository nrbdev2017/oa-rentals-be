from app.admin.permissions.infrastructure.repos.sa_permission_repository import SAPermissionRepository

class PermissionService:
    """Handles permission related functions"""
    perm_repo: SAPermissionRepository

    def __init__(self, perm_repo: SAPermissionRepository):
        self.perm_repo = perm_repo

    def get_all_permissions():
        return {
                'all_perms': 'all permissions'
                }
