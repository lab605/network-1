# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, verbose_name='\u5bc6\u7801'),
            preserve_default=False,
        ),
    ]
