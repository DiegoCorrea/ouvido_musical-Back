# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Life
# Create your models here.
class MAP(models.Model):
    life_id = models.ForeignKey(UserAverage_Life, unique=False)
    value = models.FloatField()
    at = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
