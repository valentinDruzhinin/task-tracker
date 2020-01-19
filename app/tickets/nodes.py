from graphene import relay
from .models import Ticket as TicketModel
from graphene_sqlalchemy import SQLAlchemyObjectType


class Ticket(SQLAlchemyObjectType):
    """A Ticket information"""
    class Meta:
        model = TicketModel
        interfaces = (relay.Node, )
