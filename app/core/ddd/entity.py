from dataclasses import dataclass
import uuid

@dataclass
class Entity:
  """A base class for all entities"""

  """UUID generator"""
  id: uuid.UUID

  @classmethod
  def get_id(cls) -> uuid.uuid4:
    """Generates new UUID"""
    return uuid.uuid4()

