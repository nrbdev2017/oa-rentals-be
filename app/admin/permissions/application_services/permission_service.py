from app.admin.permissions.domain.repos.permission_repository import PermissionRepository

class PermissionService:
    def get_all_permissions():
        perm_repo = PermissionRepository
        return {
                'all_perms': 'all permissions'
                }
