# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-19 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0012_task_search_params'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profiles',
            new_name='Profile',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='scrapper_profile',
        ),
    ]
