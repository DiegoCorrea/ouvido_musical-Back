# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageLife


class NDCG(models.Model):
    life = models.ForeignKey(UserAverageLife, unique=False, on_delete=models.CASCADE)
    value = models.FloatField()
    at = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
