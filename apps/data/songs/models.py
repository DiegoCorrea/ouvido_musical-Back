# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.CharField(max_length=255, unique=True, db_index=True,
                            primary_key=True, default=uuid.uuid1().hex)
    title = models.CharField(max_length=511, unique=False)

    def getSimilaries(self, songIDList):
        return self.SongSimilarity_right.filter(songBase__in=songIDList).order_by('similarity') | self.SongSimilarity_left.filter(songCompare__in=songIDList).order_by('similarity')

    def as_json(self):
        return dict(
            song_id=self.id,
            title=self.title,
        )

class SongSimilarity(models.Model):
    # IDS
    songBase = models.ForeignKey(Song, unique=False, related_name='SongSimilarity_right')
    songCompare = models.ForeignKey(Song, unique=False, related_name='SongSimilarity_left')
    # Datas
    similarity = models.FloatField(default=0.0, unique=False)
    # Timers
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('songBase', 'songCompare'),)

    def as_json(self):
        return dict(
            songBase=self.songBase,
            songCompare=self.songCompare,
            similarity=self.similarity
        )
