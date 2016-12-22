# coding=utf-8
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    # url(r'^runcommand/$', staff_member_required(deploy_something), name="deploy-sth"),
]
