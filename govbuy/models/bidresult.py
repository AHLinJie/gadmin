# coding=utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from core.models import BaseModel

import logging

logger = logging.getLogger(__name__)


class BidResult(BaseModel):
    OTHER_BID = 'other'
    ENQUIRY_BID = 'enquiry'
    SINGLE_BID = 'single'
    COMPETITIVE_BID = 'competitive'
    INVITE_BID = 'invite'
    PUBLICITY_BID = 'publicity'
    BID_BUY_TYPE = (
        (PUBLICITY_BID, u'公开招标'),
        (INVITE_BID, u'邀请招标'),
        (COMPETITIVE_BID, u'竞争性谈判'),
        (SINGLE_BID, u'单一来源采购'),
        (ENQUIRY_BID, u'询价'),
        (OTHER_BID, u'其他'),
    )
    project_id = models.IntegerField(db_index=True, unique=True, verbose_name=u'项目id')
    project_name = models.CharField(max_length=128, verbose_name=u'项目名称')
    publicity_time = models.DateTimeField(blank=True, null=True, verbose_name=u'公示时间')
    org_id = models.IntegerField(blank=True, null=True, verbose_name=u'招标机构id')
    org_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'招标机构')
    winner_org_id = models.IntegerField(blank=True, null=True, verbose_name=u'中标机构id')
    winner_org_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'中标机构')
    bid_open_time = models.DateTimeField(verbose_name=u'开标时间')
    bid_win_time = models.DateTimeField(blank=True, null=True, verbose_name=u'中标时间')
    winner_aptitude = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'中标单位资质')
    budget = models.IntegerField(default=0, verbose_name=u'项目预算')
    bid_money = models.IntegerField(default=0, verbose_name=u'中标价格')
    bid_buy_type = models.CharField(max_length=16, choices=BID_BUY_TYPE, verbose_name=u'采购方式')
    agency_org_id = models.IntegerField(blank=True, null=True, verbose_name=u'招标代理机构id')
    agency_org = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'招标代理机构')
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        db_table = "bid_analysis"
        app_label = u'govbuy'
        verbose_name = u"中标结果表"
        verbose_name_plural = u"中标结果列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.project_name)
