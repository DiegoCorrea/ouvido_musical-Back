# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Song
from .models import UserPlaySong

admin.site.register(Song)
admin.site.register(UserPlaySong)
