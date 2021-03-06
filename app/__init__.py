import hashlib
import os
from flask import Flask
from functools import partial
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.auth import auth
from app.signer import Signer
from config import get_config


env = os.getenv('ENVIRONMENT', 'local')
config = get_config(env)
db = SQLAlchemy(engine_options={
    'isolation_level': 'REPEATABLE_READ'
})


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # use g. or app_context
    db.init_app(app)
    Migrate(app, db)
    app.db = db
    from app.models import sql_alchemy
    from app.repositories.dashboards.sql_alchemy import SqlAlchemyDashboardsRepository
    from app.repositories.tickets.sql_alchemy import SqlAlchemyTicketsRepository
    from app.repositories.users.sql_alchemy import SqlAlchemyUsersRepository

    app.tickets_repository = SqlAlchemyTicketsRepository(app.db)
    app.dashboard_repository = SqlAlchemyDashboardsRepository(app.db)
    app.users_repository = SqlAlchemyUsersRepository(app.db)
    app.pass_encoder = partial(hashlib.blake2b, key=b'secret_key')
    app.signer = Signer()
    app.before_request(auth)

    from app.urls import URLS
    for endpoint in URLS:
        app.route(endpoint.url, **endpoint.optional_params)(endpoint.view)
    return app
