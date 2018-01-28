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

    def getSimilaries(self, songIDList):
        right_b = self.SongSimilarity_right.filter(songBase_id__in=songIDList)
        right_c = self.SongSimilarity_right.filter(
            songCompare_id__in=songIDList
        )
        left_b = self.SongSimilarity_left.filter(songBase_id__in=songIDList)
        left_c = self.SongSimilarity_left.filter(songCompare_id__in=songIDList)
        return (((left_c | left_b) | right_c) | right_b)

    def as_json(self):
        return dict(
            song_id=self.id,
            title=self.title,
        )


class SongSimilarity(models.Model):
    # IDS
    songBase = models.ForeignKey(
        Song, unique=False, related_name='SongSimilarity_right'
    )
    songCompare = models.ForeignKey(
        Song, unique=False, related_name='SongSimilarity_left'
    )
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
