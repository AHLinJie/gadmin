# coding=utf-8
from __future__ import unicode_literals, absolute_import
from core.models import BaseModel
from django.db import models
import logging

logger = logging.getLogger(__name__)


class ProContract(BaseModel):
    PURCHASE_TYPE = 'purchase'
    CONSTRUCTION_TYPE = 'construction'
    TRANSPORT_TYPE = 'transport'
    TECHNOLOGY_TYPE = 'technology'
    CONTRACT_TYPE = (
        (PURCHASE_TYPE, u'采购合同'),
        (CONSTRUCTION_TYPE, u'建设合同'),
        (TRANSPORT_TYPE, u'运输合同'),
        (TECHNOLOGY_TYPE, u'技术合同'),
    )
    project_id = models.IntegerField(db_index=True, verbose_name=u'项目id')
    project_name = models.CharField(max_length=128, verbose_name=u'项目名称')
    contract_type = models.CharField(max_length=16, choices=CONTRACT_TYPE, verbose_name=u'合同类型')
    first_party = models.CharField(max_length=64, verbose_name=u'甲方')
    first_party_org_id = models.IntegerField(blank=True, null=True, verbose_name=u'甲方机构id')
    second_party = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'乙方')
    second_party_org_id = models.IntegerField(blank=True, null=True, verbose_name=u'乙方机构id')
    signed_at = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'签订地点')
    signed_time = models.DateTimeField(blank=True, null=True, verbose_name=u'签订日期')
    document_person = models.CharField(max_length=16, blank=True, null=True, verbose_name=u'制单员')
    start_time = models.DateTimeField(blank=True, null=True, verbose_name=u'合同开始日期')
    end_time = models.DateTimeField(blank=True, null=True, verbose_name=u'合同结束日期')
    item_content = models.CharField(max_length=10240, blank=True, null=True, verbose_name=u'条款内容')
    is_print = models.BooleanField(default=False, verbose_name=u'是否打印')
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        db_table = "bid_pro_contract"
        app_label = u'govbuy'
        verbose_name = u"项目合同表"
        verbose_name_plural = u"项目合同列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.project_name)
