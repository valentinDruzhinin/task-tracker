from app.views.board import board
from app.views.boards import boards
from app.views.ticket import ticket
from app.views.tickets import tickets
from app.views.users import users
from app.views.logout import logout
from app.views.index import index
from app.views.register import register
from app.views.login import login


class URL:
    def __init__(self, url, view, **params):
        self.url = url
        self.view = view
        self.optional_params = params


URLS = (
    URL('/', index),
    URL('/register', register, methods=['POST', 'GET']),
    URL('/login', login, methods=['POST', 'GET']),
    URL('/logout', logout, methods=['GET']),
    URL('/users/<int:user_id>', users, methods=['GET']),
    URL('/boards', boards, methods=['GET', 'POST']),
    URL('/boards/<int:board_id>', board, methods=['GET', 'PUT', 'DELETE']),
    URL('/boards/<int:board_id>/tickets', tickets, methods=['GET', 'POST']),
    URL('/boards/<int:board_id>/tickets/<int:ticket_id>', ticket, methods=['GET', 'PUT', 'DELETE']),
)
