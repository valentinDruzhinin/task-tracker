import app
import os


DEBUG = os.environ.get('DEBUG', True)
app = app.create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG)
