from __future__ import unicode_literals
import uuid
from django.db import models

from apps.data.songs.models import Song


class CosineSimilarity_SongTitle(models.Model):
    # IDS
    songBase = models.ForeignKey(
        Song,
        unique=False,
        related_name='CosineSimilarity_SongTitle_right'
    )
    songCompare = models.ForeignKey(
        Song,
        unique=False,
        related_name='CosineSimilarity_SongTitle_left'
    )
    # Datas
    similarity = models.FloatField(default=0, unique=False)
    # Timers
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('songBase', 'songCompare'),)

    def as_json(self):
        return dict(
            songBase=self.songBase,
            songCompare=self.songCompare,
            similarity=self.similarity
        )
