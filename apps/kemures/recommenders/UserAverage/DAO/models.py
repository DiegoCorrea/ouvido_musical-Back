# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.kemures.kernel.round.models import Round
from apps.metadata.songs.models import Song
from apps.metadata.users.models import User


class UserAverageRecommendations(models.Model):
    # ID
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, unique=False, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, unique=False, on_delete=models.CASCADE)
    # Data
    similarity = models.FloatField(default=0.0, unique=False)
    relevance_like = models.BooleanField(default=False)
    relevance_score = models.IntegerField(blank=True, null=True, unique=False)

    class Meta:
        unique_together = (('user', 'song'),)
