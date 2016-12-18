# coding=utf-8
from __future__ import absolute_import, unicode_literals
import re
import os
import jieba
import subprocess
import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from scrapyd_api import ScrapydAPI

from .models import CrawlPage, Organization, GovProject
from wordutil.constans import JIEBA_CUSTOM_LIBS
from wordutil.apis.v1.diclib import word_dict_lib
from wordutil.apis.v1.govproattrsyn import add_synonym_word_2_db

from .apis.v1.govproject import get_gov_project_model_fields, add_gov_project
from .apis.v1.organization import add_organization


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


@csrf_exempt
def add_word_2_jieba_dic(request):
    # type: (HttpRequest) -> HttpResponse
    """
    添加词组到结巴词库文件
    """
    word = request.POST.get('word')
    lib_choice = request.POST.get('lib_choice')
    code, tail = word_dict_lib(word, lib_choice)
    if code:
        info = '添加成功!'
    else:
        info = '已经添加过了!'
    return HttpResponse(json.dumps({'code': 0, 'info': info, 'data': tail}))


@csrf_exempt
def add_synonym_word(request):
    # type: (HttpRequest) -> HttpResponse
    """
    添加　近义词数据
    """
    synonym_word = request.POST.get('synonym_word')
    attname = request.POST.get('attname')
    code, _, _ = add_synonym_word_2_db(synonym_word, attname)
    if code:
        info = '添加成功!'
    else:
        info = '已经添加过了!'
    return HttpResponse(json.dumps({'code': 0, 'info': info}))


@csrf_exempt
def add_organization_info(request):
    # type: (HttpRequest) -> HttpResponse
    """
    添加　机构信息
    """
    org_name = request.POST.get('org_name')
    org_type = request.POST.get('org_type')
    code, _ = add_organization(org_name, org_type)
    if code:
        info = '添加成功!'
    else:
        info = '已经添加过了!'
    return HttpResponse(json.dumps({'code': code, 'info': info}))


@csrf_exempt
def add_project_info(request):
    # type: (HttpRequest) -> HttpResponse
    """添加　招标项目信息
    """
    name = request.POST.get('name')
    issue_date = request.POST.get('issue_date')
    kwargs = {}
    for k in request.POST.keys():
        kwargs[k] = request.POST.get(k)
    kwargs.pop('name')
    kwargs.pop('issue_date')
    if not (name and issue_date):
        return HttpResponse(json.dumps({'code': 1, 'info': '参数错误!'}))
    code, _ = add_gov_project(name, issue_date, **kwargs)
    if code:
        info = '添加成功!'
    else:
        info = '已经添加过了!'
    return HttpResponse(json.dumps({'code': code, 'info': info}))


def get_project_crawl_content_verify(request):
    # type: (HttpRequest) -> HttpResponse
    craw_page_id = request.GET.get('craw_page_id')
    if craw_page_id:
        crawl = CrawlPage.objects.filter(id=craw_page_id).first()
    else:
        crawl = CrawlPage.objects.all().order_by('-created').first()
    org_types = Organization.ORG_TYPES

    # 加载jieba词典
    for lib in JIEBA_CUSTOM_LIBS:
        prodict = os.path.join(settings.STATICFILES_DIRS[0], 'jiebadic', lib[0])
        try:
            jieba.load_userdict(prodict)
        except IOError:
            continue
    fields = []
    fs = get_gov_project_model_fields()
    for f in fs:
        if f.attname not in ['id', 'created', 'modified', 'memo', 'accessory']:
            fields.append({'attname': f.attname, 'verbose_name': f.verbose_name})
    fenci_data = ''
    if not crawl:
        return render(request, 'crawPageContent.html', {})
    if crawl.html_source_code:
        crawl.html_source_code = crawl.html_source_code.replace(u'\xa0', '')
        regex = re.compile(r'[\n\r\t；（）。、：，的]')  # 去除换行 回车 制表符 中文标点符号
        t = regex.sub("", crawl.html_source_code)
        fenci_data = jieba.tokenize(t)  # 结巴分词
    return render(request, 'crawPageContent.html', {'crawl': crawl,
                                                    'org_types': org_types,
                                                    'fenci_data': fenci_data,
                                                    'qualification_types': GovProject.QUALIFICATION_TYPE,
                                                    'pro_progress': GovProject.PRO_PROGRESS,
                                                    'dict_libs': JIEBA_CUSTOM_LIBS,
                                                    'fields': fields
                                                    })
