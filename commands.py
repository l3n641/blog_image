import click
from requests_html import HTMLSession
from flask.cli import with_appcontext
from app.extensions import db


@click.command()
@with_appcontext
def spider():
    from app.servives import image_srv

    session = HTMLSession()
    page = 1
    while True:
        url = 'https://www.apptu.cn/wp-admin/admin-ajax.php?action=getpost&paged=' + str(page)
        response = session.get(url)
        datas = response.json()
        if not datas:
            return True
        for data in datas:
            image_srv.save(url=data.get('message'), img_id=data.get('id'), bookmarked=data.get('bookmarked'))
        db.session.commit()
        page = page + 1
        print(url)
