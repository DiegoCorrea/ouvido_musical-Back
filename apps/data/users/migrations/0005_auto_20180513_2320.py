# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-13 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180512_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(db_index=True, default='3bbd6f17570411e881f2b9463adf3ccc', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
