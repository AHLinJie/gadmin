# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging
from django.db import models

logger = logging.getLogger(__name__)


class BaseManager(models.Manager):
    def get_query_set(self):
        _super = super(BaseManager, self)
        if hasattr(_super, 'get_query_set'):
            return _super.get_query_set()
        return _super.get_queryset()

    get_queryset = get_query_set


class GovHostInfoManager(BaseManager):
    def is_open_hosts(self):
        return self.get_queryset().filter(is_open=True)
