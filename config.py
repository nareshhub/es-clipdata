import os


class Config(object):
    CSRF_ENABLED = True
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEVELOPMENT = True
