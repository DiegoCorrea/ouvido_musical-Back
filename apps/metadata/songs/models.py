# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


class Song(models.Model):
    id = models.CharField(
        max_length=255, unique=True, db_index=True,
        primary_key=True, default=uuid.uuid1().hex
    )
    title = models.CharField(max_length=511, unique=False)
    album = models.CharField(max_length=511, unique=False)
    artist = models.CharField(max_length=511, unique=False)
