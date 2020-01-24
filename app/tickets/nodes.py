from graphene import relay
from app.models import Ticket
from graphene_sqlalchemy import SQLAlchemyObjectType


class TicketNode(SQLAlchemyObjectType):
    """A Ticket information"""
    class Meta:
        model = Ticket
        interfaces = (relay.Node, )
