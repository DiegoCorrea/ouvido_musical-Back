# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('songs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlaySong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_count', models.IntegerField(default=0)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userplaysong',
            unique_together=set([('user', 'song')]),
        ),
    ]