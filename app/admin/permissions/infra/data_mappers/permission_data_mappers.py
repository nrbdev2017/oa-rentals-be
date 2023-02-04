from infra.models import PermissionModel
from domain.entities import Permission

def perm_model_to_entity(instance: PermissionModel) -> Permission:
       return Permission(
        id=instance.id,
        a_name=instance.a_name,
        a_code=instance.a_code,
        qualified_function=instance.qualified_function,
        a_status=instance.a_status,
    )

def perm_entity_to_model(perm: Permission, existing=None) -> PermissionModel:
       return PermissionModel(
        id=perm.id,
        a_name=perm.a_name,
        a_code=perm.a_code,
        qualified_function=perm.qualified_function,
        a_status=perm.a_status
        
