# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-19 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0007_countrydict'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CountryDict',
            new_name='RegionDict',
        ),
    ]
