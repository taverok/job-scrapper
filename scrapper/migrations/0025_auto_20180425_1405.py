# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-25 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0024_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]