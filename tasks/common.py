from app.extensions import cerery
from app.functions import spider_image


@cerery.task
def spider():
    from app.servives import image_srv
    print(image_srv.get_all())
