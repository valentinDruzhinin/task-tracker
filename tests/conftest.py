import pytest
from graphene.test import Client
from app import create_app
from app.schema import schema


@pytest.fixture(autouse=True, scope='session', name='client')
def init_client():
    app = create_app()
    with app.app_context():
        yield Client(schema=schema)
