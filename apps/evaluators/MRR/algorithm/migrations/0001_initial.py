# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-28 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userAverange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MRR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('at', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('life', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAverange.UserAverage_Life')),
            ],
        ),
    ]
