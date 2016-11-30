# coding=utf-8
from __future__ import unicode_literals, absolute_import
from core.models import BaseModel
from django.db import models
import logging

logger = logging.getLogger(__name__)


class ProCarry(BaseModel):
    TRANSPORTATION_TYPE = 'transportation'
    MATERIAL_TYPE = 'material'
    INSTALL_TYPE = 'install'
    MANUAL_TYPE = 'manual'
    OTHER_TYPE = 'other'
    CARRY_TYPE = (
        (TRANSPORTATION_TYPE, u'运输'),
        (MATERIAL_TYPE, u'物料'),
        (INSTALL_TYPE, u'安装'),
        (MANUAL_TYPE, u'人工'),
        (OTHER_TYPE, u'其他'),
    )
    project_id = models.IntegerField(db_index=True, verbose_name=u'项目id')
    project_name = models.CharField(max_length=128, verbose_name=u'所属项目名称')
    carry_type = models.CharField(max_length=16, choices=CARRY_TYPE, verbose_name=u'记录类型')
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'名称')
    sku = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'规格')
    sku_desc = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'规格描述')
    num = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'数量')
    cost = models.IntegerField(default=0, verbose_name=u'成本')
    selling_price = models.IntegerField(default=0, verbose_name=u'售价')
    label_price = models.IntegerField(default=0, verbose_name=u'标价')
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        unique_together = ('project_id', 'name')
        db_table = "bid_pro_carry"
        app_label = u'govbuy'
        verbose_name = u"收益核算明细表"
        verbose_name_plural = u"收益核算明细列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)
