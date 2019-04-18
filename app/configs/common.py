# -*- coding: utf-8 -*-

import os
from datetime import timedelta


class Common:
    SECRET_KEY = os.getenv("SECRET_KEY")

    TRANS_COMMENT = "automation"

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_IGNORE_RESULT = True

    CELERY_IMPORTS = (
        'tasks.beat'
    )
    CELERYBEAT_SCHEDULE = {
        'spider': {
            "task": "tasks.beat.spider",
            'schedule': timedelta(hours=1),
            'args': None
        }
    }
