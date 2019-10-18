class Config:
    DB_NAME = 'task_tracker'
    DB_USER = 'admin'
    DB_PASSWORD = 'mypassword'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/task_tracker'
    SQLALCHEMY_DATABASE_URI = DSN
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_config(env):
    return Config()
