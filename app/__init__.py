# -*- coding: utf-8 -*-

import logging

from flask import Flask
from app.extensions import db, migrate, cerery, redis
from app import imgs
from commands import spider


def create_app(object_name):
    app = Flask(__name__)

    app.config.from_object("app.configs.%s.Config" % object_name)

    app.logger.setLevel(logging.INFO)
    db.init_app(app)
    migrate.init_app(app, db)
    imgs.init_app(app)
    register_commands(app)
    register_shell_context(app)
    cerery.init_app(app)
    redis.init_app(app)

    return app


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_commands(app):
    commands = [spider]
    for command in commands:
        app.cli.add_command(command)
