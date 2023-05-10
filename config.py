import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = "{{secret_key}}"

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'sqlite:///simple_app.db'

class Config(object):
    APP_NAME = 'SimpleMovies'
    STATIC_FOLDER = os.path.join(BASE_DIR, 'app', 'static')
