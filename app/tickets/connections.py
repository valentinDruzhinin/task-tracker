from graphene import relay
from .nodes import Ticket


class TicketConnection(relay.Connection):
    """A Ticket Connection"""
    class Meta:
        node = Ticket
