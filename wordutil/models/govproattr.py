# coding=utf-8
from __future__ import unicode_literals, absolute_import
from core.models import BaseModel
from django.db import models
from .managers.govproattrsyn import GovProAttrSynManager
import logging

logger = logging.getLogger(__name__)


class GovProAttrSyn(BaseModel):
    main_word = models.CharField(max_length=64, db_index=True, verbose_name='主词', help_text='属性字段名称')
    attribute_field = models.CharField(max_length=32, verbose_name='属性字段')
    synonym_word = models.CharField(max_length=64, verbose_name='近义词')
    valid = models.BooleanField(default=True, verbose_name='是否有效')
    object = GovProAttrSynManager()

    class Meta:
        unique_together = ('main_word', 'synonym_word')
        db_table = "wordutil_govpro_attrsyn"
        app_label = u'wordutil'
        verbose_name = u"属性近义词表"
        verbose_name_plural = u"属性近义词列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.main_word)


class GovProAttrExclude(BaseModel):
    main_word = models.CharField(max_length=64, db_index=True, verbose_name='主词', help_text='属性字段名称')
    attribute_field = models.CharField(max_length=32, verbose_name='属性字段')
    exclude_word = models.CharField(max_length=64, verbose_name='排斥词')
    valid = models.BooleanField(default=True, verbose_name='是否有效')
    object = GovProAttrSynManager()

    class Meta:
        unique_together = ('main_word', 'exclude_word')
        db_table = "wordutil_govpro_attr_exclude_word"
        app_label = u'wordutil'
        verbose_name = u"属性排斥词表"
        verbose_name_plural = u"属性排斥词列表"

    def __unicode__(self):
        return u'%s-%s' % (self.id, self.main_word)
