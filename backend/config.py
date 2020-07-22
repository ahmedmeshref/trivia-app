import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRETKEY')
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRESQL') + 'trivia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRESQL') + 'trivia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# class ProductionConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'

class TestingConfig(Config):
    SECRET_KEY = 'testmyplantapp'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRESQL') + 'trivia'


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}