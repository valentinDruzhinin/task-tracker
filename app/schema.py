from graphene import ObjectType, Schema, relay
from app.users.connections import UserConnection
from app.dashboards.connections import DashboardConnection
from app.tickets.connections import TicketConnection
from graphene_sqlalchemy import SQLAlchemyConnectionField


class Query(ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(UserConnection)
    dashboards = SQLAlchemyConnectionField(DashboardConnection)
    tickets = SQLAlchemyConnectionField(TicketConnection)


schema = Schema(query=Query)
