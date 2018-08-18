# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.metadata.songs.models import Song
from apps.metadata.users.models import User


class ContentBasedMetadata(models.Model):
    # IDS
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, unique=False, on_delete=models.CASCADE)
    # Data
    similarity = models.FloatField(default=0.0, unique=False)
    iLike = models.BooleanField(default=False)
    score = models.IntegerField(default=0, blank=True, null=True, unique=False)
    # Timers
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'song'),)
