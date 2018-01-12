# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.evaluators.NDCG.algorithm.models import NDCG
# Create your models here.
class BenchNDCG(models.Model):
    id = models.OneToOneField(NDCG)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
