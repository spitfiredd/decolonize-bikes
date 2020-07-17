import time
import os
import shutil
from flask import Flask

from server.extensions import cors, db, migrate, ma

from server.api import models


def create_app(config='server.config'):
    app = Flask(__name__)
    app.config.from_object(config)

    app.logger.info(app.config['SQLALCHEMY_DATABASE_URI'])

    register_extensions(app)
    register_blueprints(app)


    @app.cli.command('teardown')
    def teardown():
        app.logger.info("Dropping Database")
        try:
            db.drop_all()
        except:
            app.logger.info("No tables detected.")
        app.logger.info("Dropping Alembic table")

        migrations = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  r'../migrations')
        app.logger.info(f"Migrations Folder: {migrations}")
        app.logger.info(f"Migrations folder exists: {os.path.exists(migrations)}")

        app.logger.info("Removing migrations folder.")
        try:
            shutil.rmtree(migrations)
        except FileNotFoundError:
            app.logger.info("Migrations folder does not exists.")
        app.logger.info(f"Migrations folder exists: {os.path.exists(migrations)}")

        try:
            db.engine.execute("DROP TABLE alembic_version")
        except:
            app.logger.info("Alemic Table does not exists.")

    return app


def register_extensions(app):
    cors.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from .api.views import api_bp, API_VERSION_V1

    app.register_blueprint(
        api_bp,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['API_URL_PREFIX'],
            version=API_VERSION_V1
        )
    )
