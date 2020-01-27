from graphene import relay
from .nodes import UserNode


class UserConnection(relay.Connection):
    """A User Connection"""
    class Meta:
        node = UserNode
