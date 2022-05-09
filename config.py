import os

class Config:
    """
    Class that sets the app cofiguration variables
    """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '<try-guessing-one-might-work>'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres/pitch'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+pyscopg2://billy:pass12@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    """
    Development configuration settings
    """
    DEBUG = True
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'try-guessing-one'


# config envs
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
