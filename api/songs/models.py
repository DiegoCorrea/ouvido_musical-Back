# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models


# Create your models here.
class Song(models.Model):
    id = models.CharField(max_length=255, unique=True, db_index=True,
                            primary_key=True, default=uuid.uuid1().hex)
    title = models.CharField(max_length=511, unique=False)

    def getSimilaries(self):
        return self.SongSimilarity_right.all()

    def as_json(self):
        return dict(
            song_id=self.id,
            title=self.title,
        )

class SongSimilarity(models.Model):
    songBase = models.ForeignKey(Song, unique=False, related_name='SongSimilarity_right')
    songCompare = models.ForeignKey(Song, unique=False, related_name='SongSimilarity_left')
    similarity = models.FloatField(default=0, unique=False)

    class Meta:
        unique_together = (('songBase', 'songCompare'),)

    def as_json(self):
        return dict(
            songBase=self.songBase,
            songCompare=self.songCompare,
            similarity=self.similarity
        )
