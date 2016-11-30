# coding=utf-8
from __future__ import unicode_literals, absolute_import
import logging
from ...spider_main import SpiderMain
logger = logging.getLogger(__name__)
__ALL__ = [

]


def crawl_purchase_url(route_url):
    # type: (text_type) -> None
    object_spider = SpiderMain()
    object_spider.craw(route_url)
