# coding=utf-8
from __future__ import unicode_literals, absolute_import
from .views import get_project_crawl_content_verify, add_word_2_jieba_dic, add_synonym_word, add_organization_info, \
    add_project_info, fill_crawl_content_2_gov_pro_info
from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    url(r'^vcrawl/$', get_project_crawl_content_verify, name="project-crawl-content-verify"),
    url(r'^addjiebadic/$', staff_member_required(add_word_2_jieba_dic), name="add-word-2-jieba-dic"),
    url(r'^addsynonym/$', staff_member_required(add_synonym_word), name="add-synonym-word"),
    url(r'^addorg/$', staff_member_required(add_organization_info), name="add-org"),
    url(r'^addproject/$', staff_member_required(add_project_info), name="add-project"),
    url(r'^fill/$', staff_member_required(fill_crawl_content_2_gov_pro_info), name="fill"),

]
