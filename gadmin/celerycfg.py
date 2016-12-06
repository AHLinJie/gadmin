# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging

logger = logging.getLogger(__name__)

# CELERY_RESULT_BACKEND = "amqp"    # amqp backend 将在celery 5 移除
# BROKER_URL = "amqp://guest:guest@localhost:5672//"  # 使用默认配置就好
CELERY_IMPORTS = ("tasks",)
CELERY_TASK_RESULT_EXPIRES = 300
