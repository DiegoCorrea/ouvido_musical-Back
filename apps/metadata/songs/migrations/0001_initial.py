# Generated by Django 2.1 on 2018-08-04 20:18

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
                ('id', models.CharField(db_index=True, default='8d099da8982311e89383c569513f40c7', max_length=255, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=511)),
                ('album', models.CharField(max_length=511)),
                ('artist', models.CharField(max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='SongSimilarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('songBase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SongSimilarity_right', to='songs.Song')),
                ('songCompare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SongSimilarity_left', to='songs.Song')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='songsimilarity',
            unique_together={('songBase', 'songCompare')},
        ),
    ]
