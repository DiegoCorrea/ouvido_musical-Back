# Generated by Django 2.1 on 2018-09-09 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('NDCG', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NDCGRunTime',
            fields=[
                ('id',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='NDCG.NDCG')),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
            ],
        ),
    ]
