# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Life


class MRR(models.Model):
    life = models.ForeignKey(UserAverage_Life, unique=False)
    value = models.FloatField()
    at = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
