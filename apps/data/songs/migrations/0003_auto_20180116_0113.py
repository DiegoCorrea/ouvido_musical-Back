# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-16 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20180113_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(db_index=True, default='72400b68fa5a11e7b165708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]