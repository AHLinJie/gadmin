# coding=utf-8
from __future__ import unicode_literals, absolute_import
from core.models import BaseModel
from django.db import models
import logging

logger = logging.getLogger(__name__)


class ChargePerson(BaseModel):
    CALL_BID = 'call'
    TENDER_BID = 'tender'
    CHARGE_TYPE = (
        (CALL_BID, u'招标'),
        (TENDER_BID, u'投标'),
    )
    project_id = models.IntegerField(db_index=True, verbose_name=u'项目id')
    project_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'负责项目名称')
    charge_type = models.CharField(max_length=8, choices=CHARGE_TYPE, verbose_name=u'负责类型(招/投标)')
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name=u'姓名')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name=u'电话')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name=u'邮箱')
    org_id = models.IntegerField(blank=True, null=True, verbose_name=u'机构id')
    org_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'机构名称')
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'地址')
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        unique_together = ('project_id', 'name')
        db_table = "bid_charge_person"
        app_label = u'govbuy'
        verbose_name = u"负责人表"
        verbose_name_plural = u"负责人列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)
