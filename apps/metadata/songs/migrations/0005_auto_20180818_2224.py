# Generated by Django 2.1 on 2018-08-18 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20180818_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(db_index=True, default='781a6fcca33511e8bcc87fa34c60b1da', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
