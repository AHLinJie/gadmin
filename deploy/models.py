# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from core.models import BaseModel
import logging

logger = logging.getLogger(__name__)


class DeployCil(BaseModel):
    name = models.CharField(max_length=64, verbose_name=u'部署名称')
    command = models.TextField(max_length=512, verbose_name=u'部署命令')
    is_valid = models.BooleanField(default=True, verbose_name=u'是否有效')
    memo = models.TextField(max_length=1024, blank=True, verbose_name=u'备注')

    class Meta:
        db_table = "gadmin_deploy"
        app_label = u'deploy'
        verbose_name = u"部署命令表"
        verbose_name_plural = u"部署命令列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)
