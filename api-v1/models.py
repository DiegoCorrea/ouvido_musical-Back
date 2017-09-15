# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models


# Create your models here.
class Song(models.Model):
    song = models.CharField(max_length=255, unique=True, db_index=True, 
                            primary_key=True, default=uuid.uuid1().hex)
    title = models.CharField(max_length=255, unique=False)
    album = models.CharField(max_length=255, unique=False)
    artist = models.CharField(max_length=255, unique=False)
    year = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            song_id=self.song,
            title=self.title,
            album=self.album,
            artist=self.artist,
            year=self.year
        )

class User(models.Model):
    user = models.CharField(max_length=255, unique=True, db_index=True,
                            primary_key=True, default=uuid.uuid1().hex)

    def as_json(self):
        return dict(
            user_id=self.user
        )

class UserPlaySong(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False)
    play_count = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            song_id=self.song_id,
            user_id=self.user_id,
            play_count=self.play_count
        )

class UserSongRecommendation(models.Model):
    user = models.ForeignKey(User, unique=False)
    song = models.ForeignKey(Song, unique=False)
    probabilit_play_count = models.IntegerField(default=0, unique=False)
    iLike = models.BooleanField(default=False)
    #score = models.IntegerField(null=True, blank=True)

    def as_json(self):
        return dict(
            song_id=self.song_id,
            user_id=self.user_id,
            probabilit_play_count=self.probabilit_play_count,
            iLike=self.iLike
            #score = self.score
        )

class ItemSimilarity(models.Model):
    songBase = models.ForeignKey(Song, unique=False)
    songCompare = models.CharField(max_length=255, unique=False)
    similarity = models.FloatField(default=0, unique=False)

    #class Meta:
    #    unique_together = ('songBase', 'songCompare',)

    def as_json(self):
        return dict(
            songBase=self.songBase,
            songCompare=self.songCompare,
            similarity=self.similarity
        )
