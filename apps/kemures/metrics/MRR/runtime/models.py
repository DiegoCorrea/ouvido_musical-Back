# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.kemures.metrics.MRR.algorithm.models import MRR


class MRRRunTime(models.Model):
    id = models.OneToOneField(MRR, primary_key=True, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
