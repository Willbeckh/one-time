import os


class Config:
    """
    Class that sets the app cofiguration variables
    """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '<try-guessing-one-might-work>'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # avatar configs
    AVATARS_GRAVATAR_DEFAULT = 'identicon'
    AVATARS_SIZE_TUPLE = (30, 60, 150)

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
