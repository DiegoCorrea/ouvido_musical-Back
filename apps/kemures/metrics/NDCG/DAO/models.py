# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.kemures.kernel.round.models import Round


class NDCG(models.Model):
    round = models.ForeignKey(Round, unique=False, on_delete=models.CASCADE)
    value = models.FloatField()
    at = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
