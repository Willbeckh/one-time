from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config_options

db = SQLAlchemy()  # db instance
login_manager = LoginManager()
login_manager.login_view  = 'auth.login'

def create_app(config_name):
    # flask app instance
    app = Flask(__name__)
    Bootstrap(app)

    login_manager.init_app(app)
    
    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # auth blueprint
    from .main.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # app configs
    app.config.from_object(config_options[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    # init flask extensions

    return app
