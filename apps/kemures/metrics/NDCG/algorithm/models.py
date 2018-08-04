# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.kemures.recommenders.UserAverage import UserAverage_Life


class NDCG(models.Model):
    life = models.ForeignKey(UserAverage_Life, unique=False, on_delete=models.CASCADE)
    value = models.FloatField()
    at = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
