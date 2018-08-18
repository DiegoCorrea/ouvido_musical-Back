# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


class Song(models.Model):
    id = models.CharField(
        max_length=255, unique=True, db_index=True,
        primary_key=True, default=uuid.uuid1().hex
    )
    title = models.CharField(max_length=511, unique=False)
    album = models.CharField(max_length=511, unique=False)
    artist = models.CharField(max_length=511, unique=False)


class SongSimilarity(models.Model):
    # IDS
    songBase = models.ForeignKey(
        Song, unique=False, related_name='SongSimilarity_right', on_delete=models.CASCADE
    )
    songCompare = models.ForeignKey(
        Song, unique=False, related_name='SongSimilarity_left', on_delete=models.CASCADE
    )
    # Data
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
