from __future__ import unicode_literals

from django.db import models

from apps.metadata.songs.models import Song


class CosineSimilarity(models.Model):
    # ID
    songBase = models.ForeignKey(
        Song,
        unique=False,
        related_name='CosineSimilarity_right', on_delete=models.CASCADE
    )
    songCompare = models.ForeignKey(
        Song,
        unique=False,
        related_name='CosineSimilarity_left', on_delete=models.CASCADE
    )
    # Data
    title = models.FloatField(default=0, unique=False)
    album = models.FloatField(default=0, unique=False)
    artist = models.FloatField(default=0, unique=False)

    class Meta:
        unique_together = (('songBase', 'songCompare'),)
