import os


class Config:
    DB_NAME = os.getenv('DB_NAME', 'task_tracker')
    DB_USER = os.getenv('DB_USER', 'admin')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'mypassword')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_DATABASE_URI = DSN
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_config(env):
    return Config()
