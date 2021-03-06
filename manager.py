import os
from dotenv import load_dotenv
from app import create_app
from flask import request
from app.extensions import celery

load_dotenv()

app = create_app(os.getenv("FLASK_ENV"))



@app.before_request
def before_request():
    app.jinja_env.cache = None
    if request.blueprint is not None:
        bp = app.blueprints[request.blueprint]
        if bp.jinja_loader is not None:
            newsearchpath = bp.jinja_loader.searchpath + app.jinja_loader.searchpath
            app.jinja_loader.searchpath = newsearchpath
        else:
            app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]
    else:
        app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]
