from sqlalchemy.orm import Session
from ...domain.repos.permission_repository_interface import PermissionRepositoryInterface
from ...domain.entities.permission import Permission
from ..models.permission_model import PermissionModel
from ..data_mappers.permission_data_mappers import perm_model_to_entity, perm_entity_to_model

# a sentinel value for keeping track of entities removed from the repository
REMOVED = object()

class SAPermissionRepository(PermissionRepositoryInterface):
    """SqlAlchemy implementation of PermissionRepository"""

    def __init__(self, session: Session, identity_map=None):
        self.session = session
        self._identity_map = identity_map or dict()

    def add(self, entity: Permission):
        self._identity_map[entity.id] = entity
        instance = perm_entity_to_model(entity)
        self.session.add(instance)

    def remove(self, entity: Permission):
        self._check_not_removed(entity)
        self._identity_map[entity.id] = REMOVED
        perm_model = self.session.query(PermissionModel).get(entity.id)
        self.session.delete(perm_model)

    def get_by_id(self, id):
        instance = self.session.query(PermissionModel).get(id)
        return self._get_entity(instance, perm_model_to_entity)

    def get_by_name(self, name):
        instance = self.session.query(PermissionModel).filter_by(name=name).one()
        return self._get_entity(instance, perm_model_to_entity)

    def _get_entity(self, instance, mapper_func):
        if instance is None:
            return None
        entity = perm_model_to_entity(instance)
        self._check_not_removed(entity)

        if entity.id in self._identity_map:
            return self._identity_map[entity.id]

        self._identity_map[entity.id] = entity
        return entity

    def __getitem__(self, key):
        return self.get_by_id(key)

    def _check_not_removed(self, entity):
        assert self._identity_map.get(entity.id, None) is not REMOVED, f"Entity {entity.id} already removed"

    def persist(self, entity: Permission):
        self._check_not_removed(entity)
        assert entity.id in self._identity_map, "Cannon persist entity which is unknown to the repo. Did you forget to call repo.add() for this entity?"
        instance = perm_entity_to_model(entity)
        merged = self.session.merge(instance)
        self.session.add(merged)

    def persist_all(self):
        for entity in self._identity_map:
            if entity is not REMOVED:
                self.persist(entity)
