from dataclasses import dataclass
from app.core.entities.entity import Entity
import uuid

@dataclass
class Permission(Entity):
    """Permission Entity"""
    id: uuid
    a_name: str
    a_code: str
    a_desc: str
    qualified_function: str
    a_status: str

