from abc import ABC, abstractmethod
from app.admin.permissions.domain.entities.permission import Permission

class PermissionRepositoryInterface(ABC):
    """An interface to permission repository"""

    @abstractmethod
    def add(self, entity: Permission):
        """Adds new entity to a repository"""
        raise NotImplementedError()

    # @abstractmethod
    # def delete(self, entity: Permission):
    #     """Removes existing entity from repository"""
    #     raise NotImplementedError()

    # @abstractmethod
    # def get_by_id(id: PermissionId) -> Permission:
    #    """Retrieves entity by its identity"""
    #    raise NotImplementedError()

    def __getitem__(self, index) -> Permission:
        return self.get_by_id(index)
