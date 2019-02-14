import os
import logging
from dotenv import load_dotenv


class Config:
    load_dotenv()
    ENV = os.environ.get('ENV','development')
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    SECRET_KEY = 'meow'
    LOG_LEVEL = logging.DEBUG
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME', 'session_cookie')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_CONNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    DB_CONNECTION_STRING = os.environ.get('TEST_DB_CONNECTION_STRING')


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = logging.ERROR
