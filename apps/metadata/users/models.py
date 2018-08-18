# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


class User(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        primary_key=True,
        default=uuid.uuid1().hex
    )

    def as_json(self):
        return dict(
            user_id=self.id
        )
