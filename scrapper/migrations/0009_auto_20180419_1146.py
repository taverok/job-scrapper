# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-19 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0008_auto_20180419_1144'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='regiondict',
            table='scrapper_region_dict',
        ),
    ]
