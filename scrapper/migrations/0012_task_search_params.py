# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-19 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0011_auto_20180419_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='search_params',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
