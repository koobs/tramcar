# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0005_auto_20160905_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='remote',
            field=models.BooleanField(default=False),
        ),
    ]
