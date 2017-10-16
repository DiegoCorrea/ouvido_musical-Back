# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.CharField(db_index=True, default='f748d4b9b07011e7aa05708bcdd0cf1e', max_length=255, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=511)),
                ('album', models.CharField(max_length=511)),
                ('artist', models.CharField(max_length=511)),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SongSimilarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songCompare', models.CharField(max_length=255)),
                ('similarity', models.FloatField(default=0)),
                ('songBase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Song')),
            ],
        ),
    ]