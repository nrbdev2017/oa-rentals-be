import uuid
from app.core.ddd.value_object import ValueObject

class PermissionId(ValueObject):
    id: uuid
    def __init__(self):
        self.id = uuid.uuid4()
        
