# coding=utf-8
from __future__ import unicode_literals, absolute_import
from gadmin.celery_p import app  # 这里只是pycharm 的报错飘红
from scrapyd_api import ScrapydAPI
import datetime
import logging

logger = logging.getLogger(__name__)


@app.task()
def task_spider_govbuy_list_by_spider_one_page(a=None, b=None):
    print '-' * 100
    print 'now is %s' % datetime.datetime.now()
    scrapyd = ScrapydAPI('http://localhost:6800')
    spiders = scrapyd.list_spiders('govbuyscrapy')
    print 'spider has :', spiders
    run_spider_id = scrapyd.schedule('govbuyscrapy', 'govbuy_wan_timing_list')  # 列表页面爬取
    print 'spider runner id is :', run_spider_id
    scrapyd.job_status('govbuyscrapy', run_spider_id)


@app.task()
def task_spider_govbuy_content_spider(a=None, b=None):
    print '=' * 100
    print 'now is %s' % datetime.datetime.now()
    scrapyd = ScrapydAPI('http://localhost:6800')
    spiders = scrapyd.list_spiders('govbuyscrapy')
    print 'spider has :', spiders
    run_spider_id = scrapyd.schedule('govbuyscrapy', 'govbuy_wan_timing_detail')  # 详情页面爬虫
    print 'spider runner id is :', run_spider_id
    scrapyd.job_status('govbuyscrapy', run_spider_id)
