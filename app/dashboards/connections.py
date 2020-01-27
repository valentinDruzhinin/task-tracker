from graphene import relay
from .nodes import DashboardNode


class DashboardConnection(relay.Connection):
    """A Dashboard Connection"""
    class Meta:
        node = DashboardNode
