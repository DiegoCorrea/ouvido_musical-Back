# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAverage_Recommendations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.IntegerField(default=0)),
                ('iLike', models.BooleanField(default=False)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='useraverage_recommendations',
            unique_together=set([('user', 'song')]),
        ),
    ]
