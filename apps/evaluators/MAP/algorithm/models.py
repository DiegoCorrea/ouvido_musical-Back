# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Life


class MAP(models.Model):
    life = models.ForeignKey(UserAverage_Life, unique=False, on_delete=models.CASCADE)
    value = models.FloatField()
    at = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
