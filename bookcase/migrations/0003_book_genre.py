# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-26 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcase', '0002_auto_20160626_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='unknown', max_length=200),
        ),
    ]
