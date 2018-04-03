from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, TEXT, patch_request_class


bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['UPLOADED_TEXT_DEST'] = './app/tfidf/upload_files'
    config[config_name].init_app(app)
    bootstrap.init_app(app)

    text = UploadSet('text', TEXT)
    configure_uploads(app, text)
    patch_request_class(app)

    from .tfidf import tfidf as tfidf_blueprint
    app.register_blueprint(tfidf_blueprint, url_prefix='/tfidf')

    from .sim import sim as sim_blueprint
    app.register_blueprint(sim_blueprint, url_prefix='/sim')

    from .sjet import sjet as sjet_blueprint
    app.register_blueprint(sjet_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    return app
