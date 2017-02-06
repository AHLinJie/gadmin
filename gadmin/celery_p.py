# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging
import os
from celery import Celery
from celery.schedules import crontab

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gadmin.settings')
app = Celery('gadmin')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# 注册定时任务
app.conf.beat_schedule = {
    # 'planner': {
    #     'task': 'govbuy.tasks.test_my_celery',
    #     'schedule': 10.0,
    # },

    'list_page': {
        'task': 'govbuy.tasks.task_spider_govbuy_content_spider',
        'schedule': crontab(minute='8', hour='*/1'),
        'args': (16, 16),
    },
    'content_page': {
        'task': 'govbuy.tasks.task_spider_govbuy_list_by_spider_one_page',
        'schedule': crontab(minute='0', hour='*/2'),
        'args': (16, 16),
    },
}
