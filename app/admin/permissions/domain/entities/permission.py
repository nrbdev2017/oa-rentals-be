from dataclasses import dataclass
from .value_objects.permission_id import PermissionId
from app.core.ddd.entity import Entity
import uuid

@dataclass
class Permission(Entity):
    """Permission Entity"""
    id: PermissionId 
    a_name: str
    a_code: str
    a_desc: str
    qualified_function: str
    a_status: str

    def __init__(
            self,
            id: PermissionId, 
            a_name: str, 
            a_code: str, 
            a_desc: str, 
            qualified_function: str,
            a_status: str
        ):
        self.id = id
        self.a_name = a_name
        self.a_code = a_code
        self.a_desc = a_desc
        self.qualified_function = qualified_function
        self.a_status = a_status

