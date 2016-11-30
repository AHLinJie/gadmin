# coding=utf-8
from __future__ import unicode_literals, absolute_import
from jsonfield import JSONField as JSONCharMyField
from django.db import models

import logging

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s' % self.id

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        if update_fields and 'modified' not in update_fields:
            update_fields.append('modified')
        return super(BaseModel, self).save(*args, **kwargs)
