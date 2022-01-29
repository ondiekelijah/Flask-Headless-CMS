"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOSTNAME')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}"
    SIMPLEMDE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = environ.get("SECRET_KEY")

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOSTNAME')}:{environ.get('DB_PORT')}/{environ.get('TEST_DB_NAME')}"
    TESTING = True
