# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20180106_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(db_index=True, default='6d2889eef41911e7a818708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
