# coding=utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from core.models import BaseModel
import logging

logger = logging.getLogger(__name__)


class Organization(BaseModel):
    BID_TYPE = 'bid'
    TENDER_TYPE = 'tender'
    AGENCY_TYPE = 'agency'
    ORG_TYPE = (
        (BID_TYPE, u'招标方'),
        (TENDER_TYPE, u'投标方'),
        (AGENCY_TYPE, u'代理方'),
    )
    org_type = models.CharField(max_length=8, verbose_name=u'类型')
    consistent_credit_code = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'统一信用代码')
    name = models.CharField(max_length=128, unique=True, verbose_name=u'机构名称')
    address = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'地址')
    postcode = models.CharField(max_length=6, blank=True, null=True, verbose_name=u'邮编')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name=u'联系电话')
    fax = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'传真')
    authorised_representative = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'授权代表')
    bank = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'开户银行')
    bank_no = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'开户账号')
    web_address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'网址')
    memo = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        unique_together = ('org_type', 'name')
        db_table = "bid_organization"
        app_label = u'govbuy'
        verbose_name = u"机构组织表"
        verbose_name_plural = u"机构组织列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)
