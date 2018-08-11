# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class CosineSimilarityRunTime(models.Model):
    song_model_size = models.IntegerField(default=0)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
