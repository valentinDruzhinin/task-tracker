from functools import wraps

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.models import DashboardModel
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


class RawSqlDashboardsRepository:

    def __init__(self, db):
        self.db = db

    @exceptions_wrapper
    def add(self, model: DashboardModel) -> DashboardModel:
        with self.db.begin() as conn:
            conn.execute(text(SQLQuery.CREATE_DASHBOARD), model.to_dict())
        return model

    @exceptions_wrapper
    def delete(self, model: DashboardModel) -> DashboardModel:
        with self.db.begin() as conn:
            conn.execute(text(SQLQuery.DELETE_DASHBOARD), model.id)
        return model

    @exceptions_wrapper
    def update(self, model: DashboardModel) -> DashboardModel:
        with self.db.begin() as conn:
            conn.execute(text(SQLQuery.UPDATE_DASHBOARD), model.to_dict())
        return model

    @exceptions_wrapper
    def query(self, **args) -> [DashboardModel]:
        with self.db.begin() as conn:
            return [DashboardModel(**row)
                    for row in conn.execute(
                        text(SQLQuery.GET_DASHBOARDS), DashboardModel(**args).to_dict()
                    )]
