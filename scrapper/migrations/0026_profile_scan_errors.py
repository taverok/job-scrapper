# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-25 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0025_auto_20180425_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='scan_errors',
            field=models.TextField(default=None, null=True),
        ),
    ]