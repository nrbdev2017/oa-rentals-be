from sqlalchemy.orm import relationship

from app.extensions import db, mallow
import sqlalchemy.dialects.postgresql as postgres

import uuid
from datetime import datetime


class Permission(db.Model):
    __tablename__ = 'adm_permissions'
    count_seq = db.Sequence(__tablename__ + "_count_seq")

    id = db.Column(postgres.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    a_code = db.Column(db.Text, index=True, unique=True, nullable=False)
    a_desc = db.Column(db.Text, index=True, unique=False, nullable=True)
    qualified_function = db.Column(db.Text, index=True, unique=True, nullable=False)
    a_status = db.Column(db.Text, index=True, unique=True, nullable=False)

    counter = db.Column(db.Integer, count_seq, unique=True, server_default=count_seq.next_value(), nullable=False)
    created_at = db.Column(db.DateTime(timezone=False), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=False), nullable=False)

    def __repr__(self):
        return '<Permission {}>'.format(self.created_at)


class PermissionSchema(mallow.Schema):
    class Meta:
        fields = ("id", "a_code", "a_desc", "qualified_function", "a_status", "counter", "created_at", "updated_at")
        model = Permission


perm_schema = PermissionSchema()
perms_schema = PermissionSchema(many=True)
