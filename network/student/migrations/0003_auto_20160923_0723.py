# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 23:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_id',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]