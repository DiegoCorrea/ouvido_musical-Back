# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models

from api.songs.models import Song
# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=255, unique=True, db_index=True,
                            primary_key=True, default=uuid.uuid1().hex)

    def as_json(self):
        return dict(
            user_id=self.id
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
