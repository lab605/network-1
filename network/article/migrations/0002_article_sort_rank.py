# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sort_rank',
            field=models.IntegerField(default=100, verbose_name='\u6392\u5e8f'),
        ),
    ]
