# coding=utf-8
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from scrapyd_api import ScrapydAPI
import subprocess

from celery import Celery

def get_doc_content(doc_file_name):
    # type: (text_type) -> text_type
    """获取 world 文档的文字内容
    sudo apt-get install antiword
    """
    process = subprocess.Popen(['antiword', doc_file_name], stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out, err


def call_scrapyd_service():
    """通过 api 操作爬虫
    参考文档地址：https://pypi.python.org/pypi/python-scrapyd-api#downloads
    """
    scrapyd = ScrapydAPI('http://localhost:6800')
    scrapyd.job_status('govbuyscrapy', '0c838fd4b9f111e6abcc14dda97ae760')  # 查看指定爬虫任务执行状态
    scrapyd.list_jobs('govbuyscrapy')  # 查看爬虫任务列表
    scrapyd.schedule('govbuyscrapy', 'govbuy_wan_shucheng')  # 指定项目执行指定爬虫

