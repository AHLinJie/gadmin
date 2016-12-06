# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from core.models import BaseModel
from .managers.govhostinfo import GovHostInfoManager
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
    host_url = models.CharField(max_length=128, unique=True, verbose_name=u'站点地址')
    purchase_path = models.CharField(max_length=512, blank=True, verbose_name=u'招标(采购)页面地址')
    is_open = models.BooleanField(default=True, verbose_name=u'是否可打开')
    gov_level = models.IntegerField(choices=GOV_LEVELS, verbose_name=u'等级')
    memo = models.TextField(max_length=512, blank=True, null=True, verbose_name=u'备注')
    objects = GovHostInfoManager()

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


def accessory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/detail_page/user_<id>/<filename>
    return 'crawl_pages/host_{0}_accessory/{1}'.format(instance.host_id, filename)


class CrawlPage(BaseModel):
    host_id = models.IntegerField(db_index=True, verbose_name=u'主站id')
    host_url = models.CharField(max_length=128, verbose_name=u'站点地址')
    logogram = models.CharField(max_length=64, blank=True, verbose_name=u'简写')
    project_page_url = models.CharField(max_length=512, verbose_name=u'项目页面url')
    is_crawled = models.BooleanField(default=False, verbose_name=u'是否抓取完成')
    crawl_time = models.DateTimeField(blank=True, null=True, verbose_name=u'抓取时间')
    html_source_code = models.TextField(max_length=102400, null=True, blank=True, verbose_name=u'页面原始内容')
    accessory = models.FileField(upload_to=accessory_path, blank=True, verbose_name=u'附件')

    class Meta:
        unique_together = ('host_id', 'project_page_url')
        db_table = "gov_project_crawl_page_info"
        app_label = u'govbuy'
        verbose_name = u"站点抓取信息表"
        verbose_name_plural = u"站点抓取信息列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.host_url)

    def project_page_link(self):
        if 'http' not in self.host_url:
            return ''.join(['http://', self.host_url, self.project_page_url])
        return ''.join([self.host_url, self.project_page_url])
