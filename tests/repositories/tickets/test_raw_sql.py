import pytest
from mock import Mock
from sqlalchemy.exc import SQLAlchemyError
from app.models import TicketModel
from app.queries import SQLQuery
from app.repositories.exceptions import DataBaseError
from app.repositories.tickets.raw_sql import RawSqlTicketsRepository
from tests.mocks import create_db_mock


class TestRawSqlTicketsRepository:
    ticket = TicketModel(
        id=1, title='First ticket', creator_id=1, date_of_creation='15-01-2019'
    )

    def setup_method(self):
        self.db = create_db_mock()
        self.repo = RawSqlTicketsRepository(self.db)

    # @pytest.mark.parametrize(
    #     'method,query,query_args',
    #     [
    #         (
    #             'add',
    #             SQLQuery.INSERT_TICKET,
    #             ticket.to_dict()
    #         ),
    #         (
    #             'delete',
    #             SQLQuery.DELETE_TICKET,
    #             1
    #         ),
    #         (
    #             'update',
    #             SQLQuery.UPDATE_TICKET,
    #             ticket.to_dict()
    #         )
    #     ]
    # )
    # def test_calls_db(self, method, query, query_args):
    #     actual = getattr(self.repo, method)(self.ticket)
    #
    #     self.db._con.execute.assert_called_with(query, query_args)
    #     assert self.ticket == actual
    #
    # @pytest.mark.parametrize(
    #     'method',
    #     ['add', 'delete', 'update']
    # )
    # def test_unable_to_connect_to_db(self, method):
    #     self.db.begin = Mock(side_effect=SQLAlchemyError)
    #
    #     with pytest.raises(DataBaseError):
    #         getattr(self.repo, method)(self.ticket)
    #
    # @pytest.mark.parametrize(
    #     'args',
    #     [
    #         {'id': 1},
    #         {'title': 'First ticket'},
    #         {'assignee': 1},
    #         {'creator_id': 1},
    #         {'status': 'open'},
    #     ]
    # )
    # def test_query_calls_db(self, args):
    #     self.db._con.execute = Mock(return_value=[self.ticket.to_dict()])
    #
    #     actual = self.repo.query(**args)
    #
    #     self.db._con.execute.assert_called_with(SQLQuery.GET_TICKETS, args)
    #     assert [self.ticket] == actual
    #
    # def test_query_unable_to_connect_to_db(self):
    #     self.db.begin = Mock(side_effect=SQLAlchemyError)
    #
    #     with pytest.raises(DataBaseError):
    #         self.repo.query(id=1)
