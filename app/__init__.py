from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    return app
