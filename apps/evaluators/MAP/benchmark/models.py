# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.evaluators.MAP.algorithm.models import MAP
# Create your models here.
class BenchMAP(models.Model):
    id = models.OneToOneField(MAP)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
