from app.extensions import celery
from app.functions import spider_image


@celery.task()
def spider():
    spider_image()
