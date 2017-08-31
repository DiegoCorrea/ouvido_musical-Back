# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_auto_20170830_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersongrecommendation',
            old_name='like',
            new_name='iLike',
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.CharField(db_index=True, default=b'e52bd24c8dfe11e7a6e0708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.CharField(db_index=True, default=b'e52bd24d8dfe11e7a6e0708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]