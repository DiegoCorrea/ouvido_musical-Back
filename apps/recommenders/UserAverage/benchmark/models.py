# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class BenchUserAverage(models.Model):
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
