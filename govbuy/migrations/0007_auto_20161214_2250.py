# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govbuy', '0006_auto_20161213_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawlpage',
            name='extract_type',
            field=models.CharField(choices=[('no', '\u672a\u5904\u7406'), ('manual', '\u4eba\u5de5\u63d0\u53d6'), ('machine', '\u673a\u5668\u63d0\u53d6'), ('correct', '\u4eba\u5de5\u77eb\u6b63')], db_index=True, default='machine', max_length=8, verbose_name='\u63d0\u53d6\u65b9\u5f0f'),
        ),
    ]
