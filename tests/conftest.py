import pytest
from app import create_app


# config = {
#     'dsn': 'postgresql://admin:mypassword@localhost/test'
# }
#
#
# @pytest.fixture(scope='session')
# def app():
#     app = create_app(config)
#     return app
#
#
# client = app.test_client()
# USER = {
#     'username': 'test_user',
#     'email': 'test_user_email@test',
#     'password': '12345'
# }


# @pytest.fixture()
# def client(app):
#     return app.test_client()
#
#
# @pytest.fixture(autouse=True)
# def db_fixture(app):
#     app.db.execute('TRUNCATE TABLE users')
#     yield app.db
#     app.db.execute()
