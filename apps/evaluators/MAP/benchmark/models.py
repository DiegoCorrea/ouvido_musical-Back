# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.evaluators.MAP.algorithm.models import MAP


class BenchMAP(models.Model):
    id = models.OneToOneField(MAP, primary_key=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
