# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20171016_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(db_index=True, default='ac9a7383b28611e798f8708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
