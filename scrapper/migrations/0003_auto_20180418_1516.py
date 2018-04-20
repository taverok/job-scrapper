# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-18 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_auto_20180418_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='app_id',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='app_secret',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='login',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='password',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
