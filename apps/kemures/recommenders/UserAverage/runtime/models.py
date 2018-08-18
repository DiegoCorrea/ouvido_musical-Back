# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.kemures.kernel.round.models import Round


# Create your models here.


class UserAverageRunTime(models.Model):
    round = models.OneToOneField(Round, unique=True, on_delete=models.CASCADE)
    song_set_size = models.IntegerField()
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
