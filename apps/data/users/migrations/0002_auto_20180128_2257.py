# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-28 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(db_index=True, default='94cb31f3047e11e89896708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]