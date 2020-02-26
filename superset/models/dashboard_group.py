from flask_appbuilder import Model
from superset.models.helpers import AuditMixinNullable, ImportMixin
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    UniqueConstraint,
)

class DashboardGroup(  # pylint: disable=too-many-instance-attributes
    Model, AuditMixinNullable, ImportMixin
):
    __tablename__ = "dashboard_groups"
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
