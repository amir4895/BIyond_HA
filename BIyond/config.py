import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Class configuration for Flask
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = "127.0.0.1:8081"
    DEBUG = True
    EXECUTOR_TYPE = 'process'
    EXECUTOR_MAX_WORKERS = 4
    ETL_REQUEST_TIMEOUT = 40





