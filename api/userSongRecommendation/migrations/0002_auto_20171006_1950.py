# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userSongRecommendation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersongrecommendation',
            old_name='probabilit_play_count',
            new_name='similarity',
        ),
    ]
