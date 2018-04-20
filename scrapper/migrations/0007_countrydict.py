# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-19 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0006_site_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.BigIntegerField()),
                ('country_name', models.CharField(max_length=255)),
                ('region_id', models.BigIntegerField()),
                ('region_name', models.CharField(max_length=255)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scrapper.Site')),
            ],
            options={
                'db_table': 'scrapper_country_dict',
            },
        ),
    ]
