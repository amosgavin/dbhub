# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-07 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0006_auto_20180803_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='data_type',
            field=models.CharField(blank=True, help_text='\u6570\u636e\u7c7b\u578b', max_length=100, null=True),
        ),
    ]
