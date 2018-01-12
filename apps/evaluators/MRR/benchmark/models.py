# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.evaluators.MRR.algorithm.models import MRR
# Create your models here.
class BenchMRR(models.Model):
    life = models.OneToOneField(MRR)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
