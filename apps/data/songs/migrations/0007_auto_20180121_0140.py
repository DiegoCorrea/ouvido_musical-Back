# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-21 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_auto_20180121_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(db_index=True, default='084768aafe4c11e786a0708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]