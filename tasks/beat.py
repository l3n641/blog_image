from app.extensions import cerery
from app.functions import spider_image


@cerery.task()
def spider():
    spider_image()
