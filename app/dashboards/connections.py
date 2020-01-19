from graphene import relay
from .nodes import Dashboard


class DashboardConnection(relay.Connection):
    """A Dashboard Connection"""
    class Meta:
        node = Dashboard
