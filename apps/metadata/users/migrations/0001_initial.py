# Generated by Django 2.1 on 2018-09-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(db_index=True, default='25dae67bb3dd11e8bd37708bcdd0cf1e', max_length=255,
                                        primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
