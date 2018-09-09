# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Round(models.Model):
    song_set_size = models.IntegerField()
    user_set_size = models.IntegerField()
    metadata_used = models.CharField(max_length=511, unique=False)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
