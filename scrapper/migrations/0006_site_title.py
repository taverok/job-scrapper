# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-19 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0005_auto_20180419_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
