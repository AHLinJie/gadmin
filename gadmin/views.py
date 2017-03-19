# coding=utf-8
from __future__ import unicode_literals, absolute_import
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


def rootui(request):
    return render(request, 'uibase.html')

