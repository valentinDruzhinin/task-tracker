from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from app.models.sql_alchemy import Dashboard
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


class SqlAlchemyDashboardsRepository:

    def __init__(self, db: SQLAlchemy):
        self.db = db

    @exceptions_wrapper
    def add(self, model: Dashboard) -> Dashboard:
        self.db.session.add(model)
        self.db.session.commit()
        return model

    @exceptions_wrapper
    def delete(self, model: Dashboard) -> Dashboard:
        self.db.session.delete(model)
        self.db.session.commit()
        return model

    @exceptions_wrapper
    def update(self, model: Dashboard) -> Dashboard:
        Dashboard.query.filter_by(id=model.id).update(dict(model))
        self.db.session.commit()
        return model

    @exceptions_wrapper
    def query(self, **args) -> [Dashboard]:
        return list(Dashboard.query.filter_by(**args))
