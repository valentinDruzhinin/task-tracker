from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from app.models.sql_alchemy import User
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


class SqlAlchemyUsersRepository:

    def __init__(self, db: SQLAlchemy):
        self.db = db

    @exceptions_wrapper
    def add(self, model: User) -> User:
        self.db.session.add(model)
        self.db.session.commit()
        return model

    @exceptions_wrapper
    def delete(self, model: User) -> User:
        self.db.session.delete(model)
        self.db.session.commit()
        return model

    @exceptions_wrapper
    def update(self, model: User) -> User:
        User.query.filter_by(id=model.id).update(dict(model))
        self.db.session.commit()
        return model

    @exceptions_wrapper
    def query(self, **args) -> [User]:
        return list(User.query.filter_by(**args))
