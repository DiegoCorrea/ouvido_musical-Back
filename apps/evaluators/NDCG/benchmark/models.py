# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.evaluators.NDCG.algorithm.models import NDCG


class BenchNDCG(models.Model):
    id = models.OneToOneField(NDCG, primary_key=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
