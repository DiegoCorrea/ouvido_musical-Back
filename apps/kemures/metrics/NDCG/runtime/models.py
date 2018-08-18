# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.kemures.metrics.NDCG.DAO.models import NDCG


class NDCGRunTime(models.Model):
    id = models.OneToOneField(NDCG, primary_key=True, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
