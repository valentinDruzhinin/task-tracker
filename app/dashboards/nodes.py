from graphene import relay
from .models import Dashboard as DashboardModel
from graphene_sqlalchemy import SQLAlchemyObjectType


class Dashboard(SQLAlchemyObjectType):
    """A Dashboard information"""
    class Meta:
        model = DashboardModel
        interfaces = (relay.Node, )
