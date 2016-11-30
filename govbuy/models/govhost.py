# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from core.models import BaseModel

import logging

logger = logging.getLogger(__name__)


class GovHostInfo(BaseModel):
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3
    LEVEL4 = 4

    GOV_LEVELS = (
        (LEVEL1, u'省'),
        (LEVEL2, u'市'),
        (LEVEL3, u'区'),
        (LEVEL4, u'县'),
    )

    name = models.CharField(max_length=64, unique=True, verbose_name=u'名称')
    host_url = models.CharField(max_length=128, unique=True, verbose_name=u'域名')
    purchase_path = models.CharField(max_length=512, blank=True, verbose_name=u'招标(采购)页面地址')
    gov_level = models.IntegerField(choices=GOV_LEVELS, verbose_name=u'等级')
    memo = models.TextField(max_length=512, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        db_table = "gov_host_info"
        app_label = u'govbuy'
        verbose_name = u"站点信息表"
        verbose_name_plural = u"站点信息列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)

    @property
    def purchase_url(self):
        return self.host_url + self.purchase_path
