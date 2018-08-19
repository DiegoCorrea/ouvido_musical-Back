# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Round(models.Model):
    song_set_size = models.IntegerField()
    user_set_size = models.IntegerField()
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()