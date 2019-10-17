import hashlib

from flask import Flask
from functools import partial
from sqlalchemy import create_engine
from app.auth import auth
from app.db import ISOLATION_LEVEL
from app.repositories.dashboards.raw_sql import RawSqlDashboardsRepository
from app.repositories.tickets.raw_sql import RawSqlTicketsRepository
from app.signer import Signer
from app.urls import URLS


def create_app(config):
    app = Flask(__name__)
    # use g. or app_context
    app.db = create_engine(
        config['dsn'],
        isolation_level=ISOLATION_LEVEL.REPEATABLE_READ
    )
    app.tickets_repository = RawSqlTicketsRepository(app.db)
    app.dashboard_repository = RawSqlDashboardsRepository(app.db)
    app.pass_encoder = partial(hashlib.blake2b, key=b'secret_key')
    app.signer = Signer()
    app.before_request(auth)
    for endpoint in URLS:
        app.route(endpoint.url, **endpoint.optional_params)(endpoint.view)
    return app
