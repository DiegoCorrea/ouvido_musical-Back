# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.kemures.recommenders.UserAverage.algorithm.models import UserAverage_Life

# Create your models here.
class UserAverageRunTime(models.Model):
    life = models.OneToOneField(UserAverage_Life, unique=True, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
