import click
from requests_html import HTMLSession
from flask.cli import with_appcontext
from app.extensions import db
from app.functions import spider_image


@click.command()
@with_appcontext
def spider():
    spider_image()
