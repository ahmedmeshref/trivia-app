import os 

class Config(object):
    SECRET_KEY = os.urandom(32)
    DEBUG = True
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRESQL") + 'trivia'
    SQLALCHEMY_DATABASE_URI = os.environ.get("IBM_POSTGRESQL") + 'trivia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'development'
    SQLALCHEMY_ECHO = True


# class ProductionConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'

class TestingConfig(Config):
    SECRET_KEY = 'testmyplantapp'
    TESTING = True


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}