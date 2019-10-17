from functools import wraps

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.models import TicketModel
from app.queries import SQLQuery
from logging import getLogger
from app.repositories.exceptions import DataBaseError


logger = getLogger(__name__)


def exceptions_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            logger.exception(e)
            raise DataBaseError()
    return wrapper


class RawSqlTicketsRepository:

    def __init__(self, db):
        self.db = db

    @exceptions_wrapper
    def add(self, model: TicketModel) -> TicketModel:
        with self.db.begin() as conn:
            conn.execute(text(SQLQuery.INSERT_TICKET), model.to_dict())
        return model

    @exceptions_wrapper
    def delete(self, model: TicketModel) -> TicketModel:
        with self.db.begin() as conn:
            conn.execute(text(SQLQuery.DELETE_TICKET), model.id)
        return model

    @exceptions_wrapper
    def update(self, model: TicketModel) -> TicketModel:
        with self.db.begin() as conn:
            conn.execute(text(SQLQuery.UPDATE_TICKET), model.to_dict())
        return model

    @exceptions_wrapper
    def query(self, **args) -> [TicketModel]:
        with self.db.begin() as conn:
            return [TicketModel(**row)
                    for row in conn.execute(
                        text(SQLQuery.GET_TICKETS), TicketModel(**args).to_dict()
                    )]
