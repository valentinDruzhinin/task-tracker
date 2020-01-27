from graphene import relay
from app.models import User
from graphene_sqlalchemy import SQLAlchemyObjectType


class UserNode(SQLAlchemyObjectType):
    """A User information"""
    class Meta:
        model = User
        interfaces = (relay.Node, )
