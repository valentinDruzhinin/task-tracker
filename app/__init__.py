import hashlib
import os
from flask import Flask
from functools import partial
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.auth import auth
from app.signer import Signer
from config import get_config
from flask_graphql import GraphQLView


env = os.getenv('ENVIRONMENT', 'local')
config = get_config(env)
db = SQLAlchemy(engine_options={
    'isolation_level': 'REPEATABLE_READ'
})
db.Model.query = db.session.query_property()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    Migrate(app, db)
    app.pass_encoder = partial(hashlib.blake2b, key=b'secret_key')
    app.signer = Signer()
    # app.before_request(auth)

    from app.schema import schema
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )
    return app
