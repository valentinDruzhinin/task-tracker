from graphene import relay
from .nodes import User


class UserConnection(relay.Connection):
    """A User Connection"""
    class Meta:
        node = User
