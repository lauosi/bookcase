# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-28 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcase', '0004_auto_20160628_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
