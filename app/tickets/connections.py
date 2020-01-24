from graphene import relay
from .nodes import TicketNode


class TicketConnection(relay.Connection):
    """A Ticket Connection"""
    class Meta:
        node = TicketNode
