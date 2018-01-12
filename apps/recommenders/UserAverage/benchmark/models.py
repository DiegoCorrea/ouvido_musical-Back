# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Life

# Create your models here.
class BenchUserAverage(models.Model):
    life = models.OneToOneField(UserAverage_Life)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
