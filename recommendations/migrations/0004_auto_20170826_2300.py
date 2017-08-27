# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0003_auto_20170826_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.CharField(db_index=True, default=b'62dbf4ce8ab211e7b1274c0f6e2da75d', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.CharField(db_index=True, default=b'62dbf4cf8ab211e7b1274c0f6e2da75d', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='itemsimilarity',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='usersongrecommendation',
            unique_together=set([]),
        ),
    ]