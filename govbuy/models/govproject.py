# coding=utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from core.models import BaseModel

import logging

logger = logging.getLogger(__name__)


class GovProject(BaseModel):
    STUDY_OUT = 'study_out'
    BID = 'bid'
    WIN = 'win'
    START_WORK = 'working'
    END = 'end'
    DIE = 'die'

    PRO_PROGRESS = (
        (STUDY_OUT, u'拟定'),
        (BID, u'招标中'),
        (WIN, u'中标'),
        (START_WORK, u'开工'),
        (END, u'结束'),
        (DIE, u'中止'),
    )
    PRE_QUALIFICATION = 'pre'
    POST_QUALIFICATION = 'post'
    QUALIFICATION_TYPE = (
        (PRE_QUALIFICATION, u'资格预审'),
        (POST_QUALIFICATION, u'资格后审'),
    )

    name = models.CharField(max_length=128, verbose_name=u'名称')
    issue_org_id = models.IntegerField(blank=True, null=True, verbose_name=u'发布机构id')
    issue_org_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'发布机构名称')
    issue_date = models.DateField(blank=True, null=True, verbose_name=u'发布日期')
    bid_no = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'招标编号')
    bid_person = models.CharField(max_length=128, verbose_name=u'招标人')
    bid_org_id = models.IntegerField(verbose_name=u'招标机构id')
    let_contract_time = models.DateTimeField(blank=True, null=True, verbose_name=u'开始发包时间')
    off_bid_time = models.DateTimeField(blank=True, null=True, verbose_name=u'截止投标时间')
    work_start_time = models.DateTimeField(blank=True, null=True, verbose_name=u'工期开始时间')
    work_end_time = models.DateTimeField(blank=True, null=True, verbose_name=u'工期结束时间')
    contacts_name = models.CharField(max_length=16, blank=True, null=True, verbose_name=u'联系人')
    contacts_phone = models.CharField(max_length=11, blank=True, null=True, verbose_name=u'联系人电话')
    contacts_address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'联系人地址')
    implement_address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'项目实施地点')
    project_progress = models.CharField(max_length=16, choices=PRO_PROGRESS, verbose_name=u'项目进度')
    bid_division = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'标包划分')
    budget = models.IntegerField(default=0, verbose_name=u'项目预算')
    capital_source = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'资金来源')
    qualification_requirement = models.CharField(max_length=512, blank=True, null=True, verbose_name=u'资质要求')
    qualification_type = models.CharField(default=POST_QUALIFICATION, max_length=16, choices=QUALIFICATION_TYPE,
                                          verbose_name=u'资格审查方式')
    content_desc = models.CharField(max_length=1024, blank=True, null=True, verbose_name=u'项目内容描述')
    agency_org_id = models.IntegerField(blank=True, null=True, verbose_name=u'招标代理机构id')
    agency_org_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'招标代理机构名称')
    accessory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'附件')
    memo = models.CharField(max_length=512, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        unique_together = ('name', 'issue_date')
        db_table = "bid_project"
        app_label = u'govbuy'
        verbose_name = u"招投标项目表"
        verbose_name_plural = u"招投标项目列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.name)
