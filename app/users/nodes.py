from graphene import relay
from .models import User as UserModel
from graphene_sqlalchemy import SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    """A User information"""
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
