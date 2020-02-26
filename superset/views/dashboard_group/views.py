from superset.constants import RouteMethod
from flask_appbuilder.models.sqla.interface import SQLAInterface
import superset.models.core as models
from ..base import (
    BaseSupersetView,
    check_ownership,
    DeleteMixin,
    generate_download_headers,
    SupersetModelView,
)

class DashboardGroupModelView(
    SupersetModelView, DeleteMixin
):  # pylint: disable=too-many-ancestors
    route_base = "/dashboard_group"
    datamodel = SQLAInterface(models.DashboardGroup)

    include_route_methods = RouteMethod.CRUD_SET | {
        RouteMethod.API_READ,
        RouteMethod.API_DELETE,
        "download_dashboard_groups",
    }