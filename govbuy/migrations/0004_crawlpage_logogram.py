# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('govbuy', '0003_auto_20161201_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawlpage',
            name='logogram',
            field=models.CharField(blank=True, max_length=64, verbose_name='\u7b80\u5199'),
        ),
    ]
