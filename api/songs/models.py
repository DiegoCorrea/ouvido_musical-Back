# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models


# Create your models here.
class Song(models.Model):
    id = models.CharField(max_length=255, unique=True, db_index=True,
                            primary_key=True, default=uuid.uuid1().hex)
    title = models.CharField(max_length=511, unique=False)
    album = models.CharField(max_length=511, unique=False)
    artist = models.CharField(max_length=511, unique=False)
    year = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            song_id=self.id,
            title=self.title,
            album=self.album,
            artist=self.artist,
            year=self.year
        )

class SongSimilarity(models.Model):
    songBase = models.ForeignKey(Song, unique=False, related_name='SongSimilarity_right')
    songCompare = models.ForeignKey(Song, unique=False, related_name='SongSimilarity_left')
    similarity = models.FloatField(default=0, unique=False)

    def as_json(self):
        return dict(
            songBase=self.songBase,
            songCompare=self.songCompare,
            similarity=self.similarity
        )
