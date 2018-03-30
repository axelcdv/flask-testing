from flask import Flask
from . import config


def create_app(app_config=config.BaseConfig):
    app = Flask(__name__)

    app.config.from_object(app_config)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app: Flask):
    from .core import core

    app.register_blueprint(core)


def register_extensions(app: Flask):
    from .database import db

    db.init_app(app)
