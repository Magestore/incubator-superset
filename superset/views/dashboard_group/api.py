from superset.views.base_api import BaseOwnedModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from superset.models.dashboard_group import DashboardGroup
from superset.constants import RouteMethod

class DashboardGroupRestApi(BaseOwnedModelRestApi):
    datamodel = SQLAInterface(DashboardGroup)

    include_route_methods = RouteMethod.REST_MODEL_VIEW_CRUD_SET | {
        RouteMethod.EXPORT,
        RouteMethod.RELATED,
        "bulk_delete",  # not using RouteMethod since locally defined
    }

    resource_name = "dashboard_group"
    allow_browser_login = True

    class_permission_name = "DashboardModelView"

    show_columns = [
        "title",
    ]
    order_columns = []
    list_columns = [
        "id",
        "title",
        "changed_on",
    ]