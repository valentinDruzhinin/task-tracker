import app
import os

DEBUG = os.environ.get('DEBUG', True)
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

config = {
    'dsn': f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/task_tracker'
}

if __name__ == '__main__':
    app = app.create_app(config)
    app.run(host='0.0.0.0', debug=DEBUG)
