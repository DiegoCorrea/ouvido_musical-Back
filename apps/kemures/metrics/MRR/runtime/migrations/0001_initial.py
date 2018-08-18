# Generated by Django 2.1 on 2018-08-18 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MRR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MRRRunTime',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='MRR.MRR')),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
            ],
        ),
    ]
