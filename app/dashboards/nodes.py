from graphene import relay
from app.models import Dashboard
from graphene_sqlalchemy import SQLAlchemyObjectType


class DashboardNode(SQLAlchemyObjectType):
    """A Dashboard information"""
    class Meta:
        model = Dashboard
        interfaces = (relay.Node, )
